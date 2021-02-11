from flask import Flask, render_template, request, flash
from flask_mail import Message, Mail
import folium
from folium.plugins import FastMarkerCluster
from folium.plugins import Fullscreen
from folium import FeatureGroup, LayerControl, Map, Marker
import datetime

from forms import ContactForm

import numpy as np
import pandas as pd
import geopandas
from shapely.geometry import Point

import requests
import json
import re
import urllib.request

mail = Mail()

app = Flask(__name__)

app.secret_key = '****************'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'your_email@gmail.com'
app.config["MAIL_PASSWORD"] = '****************' # password generated in Google Account Settings under 'Security', 'App passwords',
                                                 # choose 'other' in the app menu, create a name (here: 'FlaskMail'),
                                                 # and generate password. The password has 16 characters. 
                                                 # Copy/paste it under app.config["MAIL_PASSWORD"].
                                                 # It will give you access to your gmail when you have two steps verification.
mail.init_app(app)


@app.context_processor
def inject_today_date():
    return {'year': datetime.date.today().year}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


@app.route('/map')
def well_map():
    url = 'https://npdfactpages.npd.no/downloads/shape/wlbPoint.zip'
    # change path to your local directory
    urllib.request.urlretrieve(url, 'data/wlbPoint.zip')
    # change path to your local directory
    wells_explo = geopandas.read_file(
        'zip://data/wlbPoint.zip', encoding='utf-8')

    wells_explo['wlbEwDesDeg'] = wells_explo['geometry'].x
    wells_explo['wlbNsDecDeg'] = wells_explo['geometry'].y

    wells_explo_sel = wells_explo.filter(['wbName', 'well_name', 'discovery', 'field', 'prodLicenc', 'well_type', 'drilOperat',
                                          'entryYear', 'cmplYear', 'content', 'main_area', 'totalDepth', 'age_at_TD', 'fmTD',
                                          'discWelbor', 'geometry', 'wlbEwDesDeg', 'wlbNsDecDeg'],
                                         axis=1)

    wells_explo_all = wells_explo_sel.loc[wells_explo_sel['well_type'].isin([
                                                                            'EXPLORATION'])]

    map_wells = folium.Map(location=[wells_explo_all['wlbNsDecDeg'].mean(),
                                     wells_explo_all['wlbEwDesDeg'].mean()],
                           zoom_start=5,
                           tiles='cartodbpositron'
                           )

    fs = Fullscreen()

    # adding an extra map background in the layer menu
    tile = folium.TileLayer('OpenStreetMap').add_to(map_wells)

    """ defining parameters for our markers and the popups when clicking on single markers """
    callback = ('function (row) {'
                'var marker = L.marker(new L.LatLng(row[0], row[1]));'
                'var icon = L.AwesomeMarkers.icon({'
                "icon: 'star',"
                "iconColor: 'black',"
                "markerColor: 'lightgray',"
                '});'
                'marker.setIcon(icon);'
                "var popup = L.popup({maxWidth: '300'});"
                "const display_text = {text: '<b>Name: </b>' + row[2] + '</br>' + '<b> Age at TD: </b>' + row[3]};"
                "var mytext = $(`<div id='mytext' class='display_text' style='width: 100.0%; height: 100.0%;'> ${display_text.text}</div>`)[0];"
                "popup.setContent(mytext);"
                "marker.bindPopup(popup);"
                'return marker};')

    """ creating clusters with FastMarkerCluster """
    fmc = FastMarkerCluster(wells_explo_all[[
        'wlbNsDecDeg', 'wlbEwDesDeg', 'wbName', 'age_at_TD']].values.tolist(), callback=callback)
    fmc.layer_name = 'Exploration Wells'

    map_wells.add_child(fmc)  # adding fastmarkerclusters to map
    map_wells.add_child(fs)  # adding fullscreen button to map

    folium.LayerControl().add_to(map_wells)  # adding layers to map
    return map_wells._repr_html_()


if __name__ == '__main__':
    # app.run(debug=True)
    app.run("0.0.0.0", port=80, debug=False) # added host parameters for docker container