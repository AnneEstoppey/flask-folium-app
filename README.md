# flask-folium-app
By developing this app, we wished to accomplish the following:

1. Create a version 1 of an interactive well map with Folium.

2. Gain experience with the full path from a Jupyter Notebook, to a Flask app, to deployment.

PLEASE NOTE: the app is not presently online due to costs. We have deployed this app on DigitalOcean during a limited time to test it. This repo contains all necessary files for deployment.

# Project description
The well data map shows the position of all exploration wellbores on the Norwegian shelf. Wellbores are grouped into clusters when zooming out. By clicking on a wellbore position, a popup comes up with additional information. 

**Stack:** Folium, Flask (Flask-wtf, Flask-mail), Bootstrap, Docker.

<br>
    <img src="static/images/foliumapp_screenshot1.jpg" class="centerImage" width="550">
    <img src="static/images/foliumapp_screenshot2.jpg" class="centerImage" width="550">
    <img src="static/images/foliumapp_screenshot3.jpg" class="centerImage" width="550">
<br>

Additionally, there is a contact form where users can contact us with comments/suggestions.

# Data
The dataset is in the form of a shapefile which is publicly hosted by the Norwegian Petroleum Directorate, [here.](https://www.npd.no/en/about-us/information-services/available-data/map-services/)

# Future developments
* Add map functionalites and features (solve display slowness issues for polygons)

# Jupyter notebook to WebApp pipeline
Note: this pipeline is one of the many possibilities how to transform a Jupyter notebook into a web app, and deploy it. There are many other solutions. Here is the main steps we follow:

* open Jupyter notebook in **Visual Studio Code**. Clean the code (cells, comments, etc). Add functions.
* create file structure for **Flask** app (app.py, templates, static)
* add **bootstrap** for UI design
* add button and menu functionalities (UI/UX)
* create contact form with **Flask-WTF and Flask-mail**
* testing and more testing on localhost
* create **requirements.txt**
* create **DOCKERFILE**
* create **github repo** for web app files
* add a new project and droplet on **DigitalOcean**
* set up SSH access on remote
* clone repo on remote
* create **DOCKER container** on remote
* **LAUNCH APP!**

# References
**Flask app howtos**<br>
https://explore-flask.readthedocs.io/en/latest/organizing.html<br>
https://pythonhow.com/your-first-flask-website/

**Folium in Flask**<br>
https://python-visualization.github.io/folium/flask.html

**Contact form with Flask-WTF and Flask-mail**<br>
https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982<br>
https://www.youtube.com/watch?v=48Eb8JuFuUI

**Docker**<br>
https://towardsdatascience.com/how-to-deploy-your-machine-learning-web-app-to-digital-ocean-64bd19ce15e2<br>
https://www.fullstackpython.com/blog/develop-flask-web-apps-docker-containers-macos.html

**Security, DNS, SSL**<br>
https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars<br>
https://www.digitalocean.com/docs/networking/load-balancers/how-to/ssl-termination/<br>



