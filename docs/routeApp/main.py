# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:33:10 2018

@author: Jeffrey
"""

from flask import render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import googlemaps
import responses
import flask_login
import time
import os, base64
from routeApp import routeApp
from spotipy import oauth2
import spotipy

"""
mysql = MySQL()
routeApp.config['MYSQL_DATABASE_USER'] = 'root'
routeApp.config['MYSQL_DATABASE_PASSWORD'] = 'westking1'
routeApp.config['MYSQL_DATABASE_DB'] = 'photo_project'
routeApp.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(routeApp)


def extractData(query):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall() #fetches all rows of the query
    cursor.close()
    conn.close()
    return data   
"""

# user session
class User(flask_login.UserMixin):
	pass

# spotify
class spt:
    def __init__(self,username):
        client_id = os.environ["SPOTIPY_CLIENT_ID"]
        client_secret  = os.environ["SPOTIPY_CLIENT_SECRET"]
        redirect_uri  = os.environ["SPOTIPY_REDIRECT_URI"]
        scope  = 'playlist-read-private'
        cache_path  =".cache-" + username
        self.sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope, cache_path=cache_path)
        
    def auth(self):
        # oken_info = self.sp_oauth.get_cached_token()
        # f not token_info:
        auth_url  = self.sp_oauth.get_authorize_url()
        return auth_url
        
    def callback(self,url):
        code  = self.sp_oauth.parse_response_code(url)
        token_info  = self.sp_oauth.get_access_token(code)
        token=token_info['access_token']
        self.sp = spotipy.Spotify(auth=token)
        return
        
    def playlist(self):
        results = self.sp.current_user_playlists(limit=5)
        lst=[]
        for i, item in enumerate(results['items']):
            lst.append(item['name'])
        return lst

global sp
# google map api
google_client = googlemaps.Client('AIzaSyAU1Znxu_9RAGxVPj51zAenW85rYB_R1aA')
def getAL(address):
    results = google_client.geocode(address)
    return results

def getDes(point, rad):
    location = point
    radius = rad
    keyword = ''
    language = 'en-AU'
    min_price = 1
    max_price = 4
    name = ''
    open_now = True
    rank_by = 'distance'
    type_ = ''
    result = google_client.places_nearby(google_client, location, radius, keyword, language, min_price, max_price, name, open_now, rank_by, type_)
    return result
    

#begin code used for login
login_manager = flask_login.LoginManager()
login_manager.init_app(routeApp)

def get_uid():
    if flask_login.current_user.is_anonymous:
        return 0
    else:
        return 1

"login page"
@routeApp.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'GET':
        return render_template("log.html")
	#The request method is POST (page is recieving data)
    name = request.form['user']
	#Api request to get user information
    global sp 
    sp = spt(name)
    user = User()
    user.id = name
    flask_login.login_user(user)
    return redirect(url_for('main'))
    #return render_template("log.html", result="login failed*")

@routeApp.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        global sp
        if not flask_login.current_user.is_anonymous:
            data_list = sp.playlist()
            return render_template("main.html", uname=flask_login.current_user.id, username=flask_login.current_user.id, data_list = data_list)
        else:
            return redirect(url_for('log'))

@routeApp.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        return
        