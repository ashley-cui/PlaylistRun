from flask import Flask, request, Response, render_template
from flaskext.mysql import MySQL
import os.path
import api

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)


app = Flask(__name__)
# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'Rish2007'
# app.config['MYSQL_DATABASE_DB'] = 'Running_Route'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

#conn = mysql.connect()
#cursor =conn.cursor()

@app.route('/')
def index():
    content = get_file('static/index.html')
    return Response(content, mimetype="text/html")

@app.route('/api_demo')
def api_demo():
    content = get_file('static/api_demo.html')
    return Response(content, mimetype="text/html")

@app.route('/api_demo/result', methods=['GET'])
def api_demo_result():
    # print(request.args)
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    response = api.get_distance_matrix(origin, destination)

    print(response)

    status = response['rows'][0]['elements'][0]['status']

    if status == 'ZERO_RESULTS' or status == 'NOT_FOUND':
        return 'Error finding route'

    origin_formatted = response['origin_addresses'][0]
    destination_formatted = response['destination_addresses'][0]
    distance = response['rows'][0]['elements'][0]['distance']['text']
    duration = response['rows'][0]['elements'][0]['duration']['text']

    return render_template('result.html',origin=origin_formatted, destination=destination_formatted, distance=distance, duration=duration)

@app.route('/route_demo')
def route_demo():
    content = get_file('static/route_demo.html')
    return Response(content, mimetype="text/html")

@app.route('/route_demo/result', methods=['GET'])
def route_demo_result():
    # print(request.args)
    origin = request.args.get('origin')
    distance = request.args.get('distance')

    #condition


    #Direction Result Response
    #[lat,lon] float

    response = api.get_direction(origin, distance)

    print(response)

    #status = response['rows'][0]['elements'][0]['status']

    #if status == 'ZERO_RESULTS' or status == 'NOT_FOUND':
    #    return 'Error finding route'

    #origin_formatted = response['origin_addresses'][0]
    #destination_formatted = response['destination_addresses'][0]
    #distance = response['rows'][0]['elements'][0]['distance']['text']
    #duration = response['rows'][0]['elements'][0]['duration']['text']

    origin_formatted = origin
    distance_formatted = distance
    route_formatted = 'Empty Place Holder'



    return render_template('route_result.html', origin=origin_formatted, distance=distance_formatted, route=route_formatted, end_location = response)
