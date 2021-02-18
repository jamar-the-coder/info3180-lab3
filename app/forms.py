from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired()])
    email = TextField('Email', validators=[Email()])
    subject = TextField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])