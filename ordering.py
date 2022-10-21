'''
    We are using the 'Strategy' Design Pattern here to give us a variety of ways to order our flights
'''

from abc import ABC, abstractmethod

# this is like an interface in java
class OrderingStrategy(ABC):
    @abstractmethod
    def display_flights():
        pass
    
    
class AlphabeticalOrderStrategy(OrderingStrategy):
    
    def display_flights():
        pass
    
    
class LocationBasedOrderStrategy(OrderingStrategy):
    
    def display_flights():
        pass


class TimeBasedOrderStrategy(OrderingStrategy):
    
    def display_flights():
        pass