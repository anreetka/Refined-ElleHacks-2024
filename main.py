from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import requests
import os
import csv

# Import the function to collect coordinates
from coordinates import collect_coordinates_bus_shelter

load_dotenv()

app = Flask(__name__)

@app.route('/')
def map_markers():
    # Collect coordinates from the bus shelter dataset
    coordinates = collect_coordinates_bus_shelter('staticFiles/Transit-Shelter-Data.csv')
    return render_template('map.html', coordinates=coordinates, API_KEY=os.environ.get('GOOGLE_MAPS_API_KEY'))

@app.route('/calculate_route', methods=['POST'])
def calculate_route():
    data = request.json
    origin = data.get('origin', '43.851174,-79.3168389')  #( Unionville Go) Extract origin coordinates from request data
    destination = data.get('destination', '43.8339576,-79.3204871')  # (29 melville crescent, brampton)Extract destination coordinates from request data
    api_key = os.environ.get('GOOGLE_MAPS_API_KEY')

    if origin is None or destination is None:
        return jsonify({'error': 'Please provide both origin and destination coordinates.'}), 400

    if api_key is None:
        return jsonify({'error': 'Google Maps API key not found.'}), 500

    # Make a request to Google Maps Directions API
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        route_data = response.json()
        return jsonify(route_data)
    else:
        return jsonify({'error': 'Failed to fetch route data.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
