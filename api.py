import urllib.request
import os
import ssl
import json

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
