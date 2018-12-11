import urllib.request
import os
import ssl
import json
import googlemaps
from datetime import datetime
from pprint import pprint

gcloud_api_key=os.environ["GCLOUD_KEY"]
context = ssl._create_unverified_context()
google_api_root="https://maps.googleapis.com/maps/api/"

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
    #print(lat)
    #print(lng)
    #find half point
    halfLongitude = (float(distance)/2)/111
    newLat = float(lat)
    newLng = float(lng) + halfLongitude
    newLocation = str(newLat)+','+str(newLng)
    # Request directions to midpoint via walking
    now = datetime.now()
    directions_result = gmaps.directions(startAddress,str(newLat)+','+str(newLng),mode="walking",departure_time=now)
    #print(directions_result)
    return newLocation
