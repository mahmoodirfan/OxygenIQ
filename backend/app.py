from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API_KEY from the environment
API_KEY = os.getenv('API_KEY')

from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS library
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire Flask app

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
