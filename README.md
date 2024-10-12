# OxygenIQ

**OxygenIQ** is an air quality monitoring web application that provides real-time air quality data from locations around the world. It uses a clean, responsive interface to display air quality data on a map and allows users to search for air quality by inputting geographic coordinates. 

## Features

- Real-time air quality data fetching using OpenAQ API.
- Interactive map showing multiple monitoring stations.
- User-friendly interface for coordinate-based air quality search.
- Visual representation of air quality levels (AQI Legend).
- Dynamic data presentation for pollutants like PM2.5, PM10, and more.
- Styled with a modern UI and responsive design.

## Technologies Used

- **Frontend**: React.js, Leaflet.js (for maps)
- **Backend**: Flask (API proxy for OpenAQ)
- **Other**: Bootstrap, Axios (for HTTP requests)

## Getting Started

### Prerequisites
To run this project locally, ensure you have the following installed:

- Node.js (for React app)
- Python (for Flask backend)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/mahmoodirfan/OxygenIQ.git
    ```

2. Navigate to the `frontend` folder and install dependencies:
    ```bash
    cd frontend
    npm install
    ```

3. Start the frontend server:
    ```bash
    npm start
    ```

4. Navigate to the `backend` folder, set up your Flask environment and install dependencies:
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

5. Start the backend server:
    ```bash
    python app.py
    ```

### Environment Variables

You need to configure the following environment variables for the project:

- **API_KEY**: Get your OpenAQ API key and add it to the backend `.env` file.

API_KEY=<Your OpenAQ API Key>

Usage
Once both the frontend and backend are running:
Open your browser and go to http://localhost:3000 to use the app.
Enter coordinates or click on a map marker to fetch real-time air quality data.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgements
OpenAQ API for providing real-time air quality data.
Leaflet for interactive maps.
Developed by Irfan Mahmood.