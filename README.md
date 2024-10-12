**OxygenIQ - Air Quality Monitoring Application**

OxygenIQ is an interactive web application that provides real-time air quality data from various locations around the world. The app leverages the OpenAQ API to display data on pollutants like PM2.5 and PM10, and provides an intuitive, interactive map for users to select locations or input coordinates manually to retrieve air quality information.

Features
Real-Time Data: Fetch air quality data from OpenAQ, displaying pollutant levels such as PM2.5, PM10, and more.
Interactive Map: Users can select locations by clicking on an interactive map.
Manual Input: Users can also manually input latitude and longitude coordinates to fetch air quality data for specific locations.
AQI Legend: A legend that shows the Air Quality Index (AQI) categories, indicating whether the air quality is good, moderate, or hazardous.
Responsive Design: The app adapts to different screen sizes for an optimal user experience on all devices.

**Frontend:**
React: Used for building the dynamic user interface.
Leaflet.js: Used for displaying the interactive map.
Axios: Handles HTTP requests to the backend.
Bootstrap: Provides responsive styling and layout.

**Backend:**
Flask: Python web framework used to build the backend.
Flask-CORS: Handles Cross-Origin Resource Sharing, allowing the frontend to interact with the backend.
OpenAQ API: External API used to fetch real-time air quality data.

**Installation and Setup**
Prerequisites
Node.js and npm for the frontend.
Python 3 for the backend.
OpenAQ API key (stored in the .env file).

Backend (Flask)
Clone the repository:
git clone https://github.com/mahmoodirfan/OxygenIQ.git

Navigate to the backend directory:
cd backend

Install the necessary Python dependencies:
pip install -r requirements.txt

Create a .env file in the backend directory and add your OpenAQ API key:
API_KEY=your_openaq_api_key

Run the Flask backend:

python app.py

Frontend (React)
Navigate to the frontend directory:
cd frontend

Install the required dependencies using npm:
npm install

Start the frontend development server:
npm start

Usage
Open your browser and navigate to http://localhost:3000.
You can either click on the map or manually enter latitude and longitude coordinates to fetch air quality data.
View the Air Quality Index (AQI) and detailed pollutant information on the right panel of the interface.
