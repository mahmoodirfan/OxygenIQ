from app import app, db
from models import SensorData

with app.app_context():
    # Sample data
    data_points = [
        {
            'parameter': 'Air Quality',
            'value': 75.5,
            'longitude': 72.8777,
            'latitude': 19.0760,  # Mumbai
        },
        {
            'parameter': 'Water Quality',
            'value': 88.2,
            'longitude': 77.2090,
            'latitude': 28.6139,  # Delhi
        },
    ]

    for data in data_points:
        sensor_data = SensorData(
            parameter=data['parameter'],
            value=data['value'],
            longitude=data['longitude'],
            latitude=data['latitude']
        )
        db.session.add(sensor_data)

    db.session.commit()
