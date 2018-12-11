import urllib.request
import os
import ssl
import json
import googlemaps
from datetime import datetime
from pprint import pprint
from flask import Flask, request, Response, render_template
from flaskext.mysql import MySQL

gcloud_api_key=os.environ["GCLOUD_KEY"]
context = ssl._create_unverified_context()
google_api_root="https://maps.googleapis.com/maps/api/"

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Rish2007'
app.config['MYSQL_DATABASE_DB'] = 'Running_Route'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor =conn.cursor()

def get_distance_matrix(origin, destination, units="metric", languages="en"):
    params = [
        ("units",units),
        ("origins", origin),
        ("destinations", destination),
        ("key", gcloud_api_key),
        ("language", languages)
    ]
    url = google_api_root + "distancematrix/json?" + urllib.parse.urlencode(params)
    contents = urllib.request.urlopen(url, context=context).read()
    data = json.loads(contents.decode('utf-8'))
    return data


#startAddress = '1 Siber Way, Boston, MA 02215'
#distance whatever
def get_direction(startAddress, distance):
    #GMAP CLIENT
    gmaps = googlemaps.Client(key= gcloud_api_key)
    #geocode the starting address
    geocode_result = gmaps.geocode(startAddress)
    #extract long and lat from the starting address
    #print(geocode_result)
    #lat = geocode_result["results"][0]["geometry"]["location"]["lat"]
    #lng = geocode_result["results"][0]["geometry"]["location"]["lng"]
    #lat = geocode_result["geometry"]["location"]["lat"]
    #lng = geocode_result["geometry"]["location"]["lng"]
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lng = geocode_result[0]["geometry"]["location"]["lng"]
    cursor.execute("SELECT mid_point_lat, mid_point_long from Running_Route.Routes Where start_point_lat = %s and start_point_long = %s and route_length = %s", (float(lat),float(lng),float(distance)))
    result = cursor.fetchall()
    halfLongitude = (float(distance)/2)/111
    newLat = 0
    newLng = 0
    if len(result) != 0:
        for x in result:
            newLat = float(x[0])
            newLng = float(x[1])
            break
    else:
        newLat = float(lat)
        newLng = float(lng) + halfLongitude
        cursor.execute("INSERT INTO Routes VALUES (%s, %s, %s, %s, %s)", (float(lat), float(lng), newLat, newLng, float(distance)))
        conn.commit()
    newLocation = str(newLat)+','+str(newLng)
    # Request directions to midpoint via walking
    now = datetime.now()
    directions_result = gmaps.directions(startAddress,str(newLat)+','+str(newLng),mode="walking",departure_time=now)
    #print(directions_result)
    return newLocation
