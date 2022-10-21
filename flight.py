
from typing import List

class Duration:
    hours: int
    minutes: int
    
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        
    def __repr__(self):
        return f'{self.hours} hours, {self.minutes} minutes'


class FlightDetails:
    plane_type: str
    start_location: str
    destination_location: str
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
    
    
    def __repr__(self):
        return f'   {self.plane_type}        {self.start_location}          {self.destination_location}        {self.total_duration}           {self.max_passengers}                {self.current_passangers}'
    
    
        
class FlightDatabase:
    flight_list: List[FlightDetails] 
    
    def __init__(self):
        self.flight_list = []
        self.create_flights()
        
    def create_flights(self):
        file = open('flights', 'r')
        for line in file.readlines():
            plane_type, start_location, destination_location, hours, mins, max_passengers, current_passengers = line.split(' ')
            self.flight_list.append(FlightDetails(plane_type, start_location, destination_location, hours, mins, max_passengers, current_passengers))
    
    def show_flights(self):
        print('|  PLANE TYPE   |   START  |  DESTINATION |     TOTAL DURATION     |  MAX PASSENGERS |  CURRENT PASSANGERS')
        for flight in self.flight_list:
            print(flight)
            
        
    
    