
class FlightData:
    def __init__(self, origin_city, destination_city, going_date, origin_airport, destination_airport, return_date, price, stop_overs = 0, via_city= ""):
        self.origin_city = origin_city 
        self.destination_city = destination_city
        self.going_date = going_date
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.return_date = return_date
        self.price = price

        self.stop_overs = stop_overs
        self.via_city = via_city
