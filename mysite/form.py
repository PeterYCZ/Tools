from flask_wtf import Form
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import Required,Length

class DataForm(Form):
    Year = StringField('Year:', validators =[Required(),Length(min=1, max=30)])
    Month = StringField('Month:', validators =[Required(),Length(min=1, max=30)])
    Day = StringField('Day:', validators =[Required(),Length(min=1, max=30)])
    submit = SubmitField("Confirmed")

class NameForm(Form):
    name = StringField('What is your name?',validators =[Required()])
    submit = SubmitField('Submit')
