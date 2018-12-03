from flask import Flask, request, Response, render_template,redirect
import os.path
import api
import spotauth

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
@app.route('/spot')
def spot():
    signin=spotauth.auth()
    return redirect(signin)
@app.route('/callback')
def callback():
    r=spotauth.songs(request.url)

    return render_template('authsuccess.html',stuff=r)


















