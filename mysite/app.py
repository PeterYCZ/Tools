from flask import render_template
from flask import Flask
from flask import request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'

class NameForm(Form):
    name = StringField('What is your name?',validators =[Required()])
    submit = SubmitField('Submit')
    def validate_on_submit(x):
        return True
 
@app.route('/',methods=['GET','POST'])
def index():
    name = None
    form = NameForm(request.form)
    if request.method == 'POST':
        name = request.form['What is your name?']
    return render_template('index.html',form=form,name=name)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)
