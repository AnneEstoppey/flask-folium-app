from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError


class ContactForm(FlaskForm):
    name = TextField("Name",  [validators.Required()])
    email = TextField("Email",  [validators.Required(
        "Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = TextField("Subject",  [validators.Required()])
    message = TextAreaField("Message",  [validators.Required()])
    submit = SubmitField("Send")
