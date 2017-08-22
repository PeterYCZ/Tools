from flask import render_template
from flask import Flask
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from form import DataForm,NameForm
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap = Bootstrap(app)

def isVaildDate(date):
    try:
       gettime = time.strptime(date, "%Y-%m-%d")
       return True
    except:
       return False

def doanything(year,month,day):
    return True

class mythread(threading.Thread):
    def __init__(self,id):
       threading.Thread.__init__(self)
       self.id = id
    def settime(self,year,month,day):
       self.year = year
       self.month = month  
       self.day = day    
    def run(self):
       doanything(self.year,self.month,self.day)
       time.sleep(10)

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
       date = Year+'-'+Month+'-'+Day
       if isVaildDate(date) == True:
           a = mythread(1)
           a.settime(Year,Month,Day)
           a.start()
           while a.is_alive() == True:
               return render_template('wait.html')
       else:
           return render_template('error.html')
       form.Year.data = ''
       form.Month.data = ''
       form.Day.data = ''
    return render_template('index.html',form=form)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/chart/')
def chart():
    return render_template('chart.html')

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)
