from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])
