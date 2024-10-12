from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API_KEY from the .env file
API_KEY = os.getenv('API_KEY')

import requests

# Function to fetch air quality data from OpenAQ
def get_air_quality_data(lat, lon):
    url = f'https://api.openaq.org/v2/latest?coordinates={lat},{lon}&radius=10000'
    
    # Add the API key to the request headers
    headers = {
        'x-api-key': API_KEY
    }

    # Make the request
    response = requests.get(url, headers=headers)
    
    # Check for successful response
    if response.status_code == 200:
        return response.json()  # Return the API data as JSON
    else:
        return {'error': f'Failed to fetch data, status code: {response.status_code}'}
