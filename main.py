# from flask import Flask, render_template, jsonify, request
# from dotenv import load_dotenv
# import requests
# from coordinates import collect_coordinates_bus_shelter
# import os

# load_dotenv()

# app = Flask(__name__)


# @app.route('/')
# def map_markers():
#     coordinates = collect_coordinates_bus_shelter('staticFiles/Transit-Shelter-Data.csv')
#     return render_template('map.html', coordinates=coordinates, API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY'))


# @app.route('/calculate_route', methods=['POST'])
# def calculate_route():
#     data = request.json
#     origin = data.get('origin', '43.7734628, -79.4926156')  # Extract origin coordinates from request data
#     destination = data.get('destination', '43.7960, -79.3897')  # Extract destination coordinates from request data
#     api_key = os.environ.get('GOOGLE_MAPS_API_KEY')

#     if origin is None or destination is None:
#         return jsonify({'error': 'Please provide both origin and destination coordinates.'}), 400

#     if api_key is None:
#         return jsonify({'error': 'Google Maps API key not found.'}), 500

#     # Make a request to Google Maps Directions API
#     url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
#     response = requests.get(url)
#     print(response)

#     if response.status_code == 200:
#         route_data = response.json()
#         return jsonify(route_data)
#     else:
#         return jsonify({'error': 'Failed to fetch route data.'}), 500



# # @app.route('/calculate_route', methods=['POST'])
# # def calculate_route():
# #     # Get the coordinates from the request data
# #     data = request.json
# #     if 'origin' not in data or 'destination' not in data:
# #         return jsonify({'error': 'Please provide both origin and destination coordinates.'}), 400

# #     origin = data['origin']
# #     destination = data['destination']
# #     api_key = os.environ.get('GOOGLE_MAPS_API_KEY')

# #     if api_key is None:
# #         return jsonify({'error': 'Google Maps API key not found.'}), 500

# #     # Make a request to Google Maps Directions API
# #     url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
# #     response = requests.get(url)

# #     if response.status_code == 200:
# #         route_data = response.json()
# #         return jsonify(route_data)
# #     else:
# #         return jsonify({'error': 'Failed to fetch route data.'}), 500


# # @app.route('/calculate_route', methods=['POST'])
# # def calculate_route():
# #     data = request.json
# #     origin= request.json.get('origin', '43.77423,  -79.50489')
# #     destination=request.json.get('destination', '34.0522, -118.2437')
# #     api_key = os.environ.get('GOOGLE_MAPS_API_KEY')

# #     route_data = {
# #         'origin': origin,
# #         'destination': destination,
# #         'transit_path': transit_path
# #     }

# #     return jsonify(route_data) 

# if __name__ == '__main__':
#     app.run(debug=True)







from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def map_markers():
    coordinates = [
        {"latitude": 43.7814368, "longitude": -79.4175989, "name": "Marker 1"},
        {"latitude": 43.7959696, "longitude": -79.3496602, "name": "Marker 2"}
    ]  # Example coordinates, replace with your actual data
    return render_template('map.html', coordinates=coordinates, API_KEY=os.environ.get('GOOGLE_MAPS_API_KEY'))

@app.route('/calculate_route', methods=['POST'])
def calculate_route():
    data = request.json
    origin = data.get('origin', '43.7814368, -79.4175989')  # Extract origin coordinates from request data
    destination = data.get('destination', '43.7959696, -79.3496602')  # Extract destination coordinates from request data
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
