class Station:
    '''Models each Station'''
    def __init__(self, name, distance, cost):
        self.name = name
        self.distance = distance 
        self.cost = cost  



class Stations:
    '''Models the Stations'''
    def __init__(self): 
        self.stations = [
            Station(name="Fatehganj", distance=10, cost=20),
            Station(name="Tisua", distance=15, cost=25),
            Station(name="Faridpur", distance=25, cost=40),
            Station(name="Rasuyia", distance=30, cost=45),
            Station(name="Bareilly", distance=40, cost=60)
        ]


    def get_stations(self):
        '''Return all the stations'''
        options = ""
        for station in self.stations:
            options = options + f'{station.name}\n'
        return options

    def find_station(self, station_name):
        '''searches for station in given stations. If exists - return the item, otherwise return None'''
        for station in self.stations:
            if station.name == station_name:
                return station

