import string
from turtle import st

class Duration:
    hours: int
    minutes: int
    
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        
    def __repr__(self):
        return f'{self.hours} hrs, {self.minutes} mins'


class FlightDetails:
    plane_type: string
    start_location: string
    destination_location: string
    total_duration: Duration
    max_passengers: int
    current_passangers: int
    
    def __init__(self, plane_type, start_location, destination_location, hours, mins, max_passengers, current_passengers):
        self.plane_type = plane_type
        self.start_location = start_location
        self.destination_location = destination_location
        self.total_duration = Duration(hours, mins)
        self.max_passengers = max_passengers
        self.current_passangers = current_passengers
        
    
    