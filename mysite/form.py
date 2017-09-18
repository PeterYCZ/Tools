from flask_wtf import FlaskForm as Form
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import Required,Length

class DataForm(Form):
    Year = StringField('Year:', validators =[Required(),Length(min=1, max=30)])
    Month = StringField('Month:', validators =[Required(),Length(min=1, max=30)])
    Day = StringField('Day:', validators =[Required(),Length(min=1, max=30)])
    submit = SubmitField("Confirmed")

class DownloadForm(Form):
    ID = StringField('ID:', validators =[Required(),Length(min=1, max=30)])
    submit = SubmitField('Download')

class ChartForm(Form):
    ID = StringField('ID:', validators =[Required(),Length(min=1, max=30)])
    BuildingID = StringField('BuildingID:', validators =[Required(),Length(min=1, max=30)])
    submit = SubmitField('Submit')

class NameForm(Form):
    name = StringField('What is your name?',validators =[Required()])
    submit = SubmitField('Submit')
