# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:33:10 2018

@author: Jeffrey
"""

from flask import render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import flask_login
import time
import os, base64
from photoApp import photoApp

mysql = MySQL()
photoApp.config['MYSQL_DATABASE_USER'] = 'root'
photoApp.config['MYSQL_DATABASE_PASSWORD'] = 'westking1'
photoApp.config['MYSQL_DATABASE_DB'] = 'photo_project'
photoApp.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(photoApp)

def extractData(query):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall() #fetches all rows of the query
    cursor.close()
    conn.close()
    return data   

# user session
class User(flask_login.UserMixin):
	pass

#begin code used for login
login_manager = flask_login.LoginManager()
login_manager.init_app(photoApp)

"login page"
@photoApp.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'GET':
        return render_template("log.html")
	#The request method is POST (page is recieving data)
    email = request.form['user']
	#Api request to get user information
    
    
    if True:
        user = User()
        user.id = email
        flask_login.login_user(user) #okay login in user
        return redirect(url_for('main'))
    return render_template("log.html", result="login failed*")

@photoApp.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        if not flask_login.current_user.is_anonymous:
            
            return render_template("main.html", uname=flask_login.current_user.id, username=flask_login.current_user.id, friends=data, albums=data_1, icon=icon, tags=tags)
        else:
            return redirect(url_for('photo_main'))
    else:
        return 

@photoApp.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        return
        