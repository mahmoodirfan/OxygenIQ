from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

db = SQLAlchemy()

class SensorData(db.Model):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True)
    parameter = Column(String)
    value = Column(Float)
    longitude = Column(Float)
    latitude = Column(Float)

    def to_dict(self):
        return {
            'id': self.id,
            'parameter': self.parameter,
            'value': self.value,
            'longitude': self.longitude,
            'latitude': self.latitude
        }
