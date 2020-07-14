from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

from app.models import User


class SubmitForm(FlaskForm):
    id = StringField("id", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    regno = StringField("Registration No.", validators=[DataRequired()])
    dpt = StringField("Department", validators=[DataRequired()])
    cgpa = StringField("CGPA", validators=[DataRequired()])
    
    submit = SubmitField("Submit")