from flask import Flask, render_template, jsonify, request, session
from dotenv import load_dotenv
from coordinates import collect_coordinates_bus_shelter
import requests
import os

load_dotenv()

app = Flask(__name__)
app.secret_key='ksidghioher8723543'
api_key = os.environ.get('GOOGLE_MAPS_API_KEY')

@app.route('/', methods=['GET'])
def formPage():
    return render_template('forms.html')

@app.route('/calculate_route',  methods=['GET', 'POST'])
def calculateRoute():
    data = request.json
    origin = data.get('source_address') 
    destination = data.get('destination_address') 

    if origin is None or destination is None:
        return jsonify({'error': 'Please provide both origin and destination coordinates.'}), 400

    if api_key is None:
        return jsonify({'error': 'Google Maps API key not found.'}), 500
    
    session['origin'] = origin
    session['destination'] = destination

    # Make a request to Google Maps Directions API
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        route_data = response.json()
        return jsonify(route_data)
    else:
        return jsonify({'error': 'Failed to fetch route data.'}), 500
    
@app.route('/map-route', methods=['GET'])
def showMap():
    origin = session.get('origin')
    destination = session.get('destination')

    addressList = [origin, destination]

    if not addressList:
        return jsonify({'error': 'Address parameter is required'}), 400

    userCoordinates = []

    for address in addressList:

        geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
        response = requests.get(geocode_url)

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'OK':
                location = data['results'][0]['geometry']['location']
                latitude = location['lat']
                longitude = location['lng']
                userCoordinates.append({'address': address, 'latitude': latitude, 'longitude': longitude})
            else:
                return jsonify ({'error': 'Failed to geocode address'}), 500
        else:
            return jsonify({'error': 'Failed to connect to geocoding service'}), 500

    coordinates = collect_coordinates_bus_shelter('staticFiles/Transit-Shelter-Data.csv')
    return render_template('map.html', coordinates=coordinates, source_loc = userCoordinates[0], dest_loc = userCoordinates[1], API_KEY=os.environ.get('GOOGLE_MAPS_API_KEY'))

     

# @app.route('/')
# def map_markers():
#     # Collect coordinates from the bus shelter dataset
#     coordinates = extractDataFromDatabase()
#     return render_template('map.html', coordinates=coordinates, API_KEY=os.environ.get('GOOGLE_MAPS_API_KEY'))

# @app.route('/calculate_route', methods=['POST'])
# def calculate_route():
#     data = request.json
#     origin = data.get('origin', '43.7729984,-79.5084078')  #(York Keele Campus) Extract origin coordinates from request data
#     destination = data.get('destination', '43.6621761,-79.3984965')  # (Uoft) Extract destination coordinates from request data
#     api_key = os.environ.get('GOOGLE_MAPS_API_KEY')

#     if origin is None or destination is None:
#         return jsonify({'error': 'Please provide both origin and destination coordinates.'}), 400

#     if api_key is None:
#         return jsonify({'error': 'Google Maps API key not found.'}), 500

#     # Make a request to Google Maps Directions API
#     url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         route_data = response.json()
#         return jsonify(route_data)
#     else:
#         return jsonify({'error': 'Failed to fetch route data.'}), 500
     
# @app.route('/api/submit-form', methods=['GET']) 
# def submit_form():
#     return render_template('demo.html')

# @app.route('/api/submit-form', methods=['POST'])
# def receive_data(): 
#     source_address = request.form.get('source_address')
#     destination_address = request.form.get('destination_address')
#     if source_address and destination_address:
#         print("Recieved Data:", source_address, destination_address)
#         return jsonify({'status': 'success', 'message': 'Data received successfully!'})
#     else:
#         return jsonify({'status': 'error', 'message': 'Invalid Data Received!'})


if __name__ == '__main__':
    app.run(debug=True)
