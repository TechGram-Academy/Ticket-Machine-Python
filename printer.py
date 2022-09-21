class Printer:
    '''Models Printer that print ticket'''
    def __init__(self):
        self.resources = {
            'paper':100,
            'ink':500
        }


    def report(self):
        '''Prints a report of all printer resources'''
        print(f"Paper: {self.resources['paper']} tickets left.")
        print(f"Ink: {self.resources['ink']} tickets left ")

    def is_resources_sufficient(self):
        '''Returns True if ticket can be printed or return False if Paper and Ink is not sufficient'''
        for key in self.resources:
            if self.resources[key] < 1:
                print(f'Sorry there is not enough {key} to print ticket.')
                return False 
        return True

    def print_ticket(self, station):
        print('------------ Ticket ------------')
        print("From: Katra")
        print(f"To: {station.name}")
        print(f"Cost: {station.cost}")
        print('--------------------------------')

        for key in self.resources:
            self.resources[key] = self.resources[key] - 1
        

      