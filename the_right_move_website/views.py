from flask import render_template
from flaskexample import app
#from sqlalchemy import create_engine
#from sqlalchemy_utils import database_exists, create_database
import pandas as pd
#import psycopg2
from flask import request 
from flaskexample.a_Model import predict_vio




@app.route('/')
@app.route('/index')
@app.route('/input')
def cesareans_input():
   return render_template("input.html")



@app.route('/output')
def cesareans_output():
 #pull 'birth_month' from input field and store it
 apt_site = request.args.get('birth_month')

 the_result = predict_vio(apt_site)
 return render_template("output.html", the_result = the_result)

@app.route('/about')
def cesareans_about():
   return render_template("about.html")

@app.route('/contact')
def cesareans_contact():
   return render_template("contact.html")

