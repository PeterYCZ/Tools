from flask import render_template
from flask import Flask
from flask import request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from form import DataForm,NameForm

app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap = Bootstrap(app)

 
@app.route('/',methods=['GET','POST'])
def index():
    Year = None
    Month = None
    Day = None
    name = None
    form = DataForm()
    if form.validate_on_submit():
       Year = form.Year.data
       Month = form.Month.data
       Day = form.Day.data
       form.Year.data = ''
       form.Month.data = ''
       form.Day.data = ''
    return render_template('index.html',form=form)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)
