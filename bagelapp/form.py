from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired,  NumberRange

class Guess(FlaskForm):
    guess=DecimalField('Guess', validators=[NumberRange(min=100, max=999, message="Please enter a three digit number!")])
    submit=SubmitField('Submit Guess')