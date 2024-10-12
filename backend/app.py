from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS library
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire Flask app

# API Key for OpenAQ API
API_KEY = '2110b57c7a15e553abdd4542f3fa60f4dbe4bc773e495b046b057e9dbbdc544d'

# Proxy route to fetch air quality stations from OpenAQ
@app.route('/api/stations', methods=['GET'])
def get_stations():
    # Increase the limit of locations and add optional filtering
    openaq_url = 'https://api.openaq.org/v2/locations?limit=1000'

    headers = {
        'x-api-key': API_KEY
    }

    try:
        response = requests.get(openaq_url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
        return jsonify(response.json())  # Send the API response to the frontend
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to fetch data: {str(e)}'}), 500


# Proxy route to fetch real-time air quality data based on coordinates
@app.route('/api/realtime-data', methods=['GET'])
def get_realtime_data():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    # Validate lat and lon inputs
    if not lat or not lon:
        return jsonify({'error': 'Missing latitude or longitude parameters'}), 400

    openaq_url = f'https://api.openaq.org/v2/latest?coordinates={lat},{lon}'

    headers = {
        'x-api-key': API_KEY
    }

    try:
        response = requests.get(openaq_url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
        return jsonify(response.json())  # Send the API response to the frontend
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to fetch data: {str(e)}'}), 500


if __name__ == '__main__':
    # Run the Flask app with debug mode enabled
    app.run(debug=True)
