from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    subject = StringField("Subject", validators=[InputRequired(), Length(min=2, max=100)])
    message = TextAreaField("Message", validators=[InputRequired(), Length(min=10)])
    submit = SubmitField("Send")
