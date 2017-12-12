from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Thing


class AddItem(FlaskForm):
    """
    Form for adding items to the database
    """
    barcode = StringField('Email', validators=[DataRequired()])
    name = StringField('Username', validators=[DataRequired()])
    description = StringField('First Name', validators=[DataRequired()])
    owner = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Add')


