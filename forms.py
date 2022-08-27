from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class ElephantForm(FlaskForm):
    search = SelectField(label="Search for:", choices=["Name", "Sex"],
                         validators=[DataRequired()])
    input = StringField(validators=[DataRequired()])
    search_button = SubmitField(label="Search")
