from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
# Task 2
@app.route('/')
def hello():
  return '<p>Juan M. : smh</p> <p>Carlos R. : fym</p> <p>John B. : tttka</p>'

# Task 3
@app.route('/jorge')
def t_test():
   return render_template('template_1.html')

# Task 4
@app.route('/j')
def t():
   return render_template('template.html')

# Task 5 GitHub Link: 

#GitHub Test