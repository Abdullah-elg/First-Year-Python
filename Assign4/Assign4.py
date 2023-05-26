from Flight import *
from Airport import *

allAirports = []
allFlights = {}
# loads data from the text files so that they can be turned into list/dictionary
def loadData(airportFile, flightFile):
    try:
        # Creates a list with all airports from the text file
        with open(airportFile,'r') as f:
            for line in f:
                textLine = line.split(",")
                list = []
                for word in textLine:
                    word = word.strip()
                    list.append(word)
                allAirports.append(Airport(list[0], list[2], list[1]))
        # Creates a dictionary with all flights from the text file
        with open(flightFile,'r') as f:
            listOfLists = []
            for line in f:
                textLine = line.split(",")
                list = []
                for word in textLine:
                    word = word.strip()
                    list.append(word)
                n = 0
                while n < len(allAirports):
                    if allAirports[n].getCode() == list[1]:
                        list[1] = allAirports[n]
                    elif allAirports[n].getCode() == list[2]:
                        list[2] = allAirports[n]
                    n += 1
                listOfLists.append(Flight(list[0], list[1], list[2]))
            for x in listOfLists:
                if x.getOrigin().getCode() not in allFlights.keys():
                    allFlights[x.getOrigin().getCode()] = [x]
                else:
                    allFlights[x.getOrigin().getCode()].append(x)
        return True
    except:
        return False

# Uses the airport code to find the city and country of said airport
def getAirportByCode(code):
    for x in allAirports:
        if x.getCode() == code:
            return x
    return -1

# Finds all flight numbers that travel from/to every airport in city
def findAllCityFlights(city):
    code = []
    for n in allAirports:
        if city == n.getCity():
            code.append(n.getCode())
    flight = []
    for x in code:
        for flightKeys, flightValues in allFlights.items():
            if x == flightKeys:
                for n in flightValues:
                    flight.append(n)
            for y in flightValues:
                if x == y.getDestination().getCode():
                    flight.append(y)
    return flight

# Finds all flight numbers that travel from/to every airport in country
def findAllCountryFlights(country):
    code = []
    for n in allAirports:
        if country == n.getCountry():
            code.append(n.getCode())
    flight = []
    for x in code:
        for flightKeys, flightValues in allFlights.items():
            if x == flightKeys:
                for n in flightValues:
                    flight.append(n)
            for y in flightValues:
                if x == y.getDestination().getCode():
                    flight.append(y)
    return flight

# If there are no direct flights from the origin to the destination, finds all airports that can be used as connecting flights
def findFlightBetween(origAirport, destAirport):
    listOfSequences = set()
    for flightKeys, flightValues in allFlights.items():
        if origAirport.getCode() == flightKeys:
            newValues = []
            for x in flightValues:
                newValues.append(x.getDestination().getCode())
            if destAirport.getCode() in newValues:
                return "Direct Flight: {} to {}".format(origAirport.getCode(), destAirport.getCode())
    for flightKeys2, flightValues2 in allFlights.items():
        if flightKeys2 in newValues:
            newValues2 = []
            for n in flightValues2:
                newValues2.append(n.getDestination().getCode())
            if destAirport.getCode() in newValues2:
                listOfSequences.add(flightKeys2)
    if len(listOfSequences) > 0:
        return listOfSequences
    else:
        return -1

# Uses the flight and finds the return flight meaning the origin becomes the destination and destination becomes the origin for the flight
def findReturnFlight(firstFlight):
    for flightKeys, flightValues in allFlights.items():
        if flightKeys == firstFlight.getDestination().getCode():
            for x in flightValues:
                if x.getDestination().getCode() == firstFlight.getOrigin().getCode():
                    return x
    return -1
