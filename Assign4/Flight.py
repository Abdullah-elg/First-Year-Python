from Airport import *
# Creates a class called Flight with flight number, origin, and destination of the flight
class Flight:
    def __init__(self, flightNo, origin, destination):
        # checks if origin and destination are objects of the airport class
        if isinstance(origin, Airport) == True and isinstance(destination, Airport) == True:
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError("The origin and destination must be Airport objects")
    def __repr__(self):
        # Checks if the flight is domestic or international then returns the respective flight
        if self.isDomesticFlight() == True:
            return "Flight: {} from {} to {} {{domestic}}".format(self._flightNo, self._origin.getCity(), self._destination.getCity())
        else:
            return "Flight: {} from {} to {} {{international}}".format(self._flightNo, self._origin.getCity(), self._destination.getCity())
    def __eq__(self, other):
        if self._origin == other.getOrigin() and self._destination == other.getDestination():
            return True
        else:
            return False
    def getFlightNumber(self):
        return self._flightNo
    def getOrigin(self):
        return self._origin
    def getDestination(self):
        return self._destination
    def isDomesticFlight(self):
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        else:
            return False
    def setOrigin(self, origin):
        self._origin = origin
    def setDestination(self, destination):
        self._destination = destination
