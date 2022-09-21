from money import Money 
from printer import Printer
from stations import Stations 

money_machine = Money()
printer = Printer()
stations = Stations()

is_on = True 

while is_on:
    options = stations.get_stations()
    print(options)
    choice = input(F"Where you want to go:")
    if choice == 'off':
        is_on = False 
    elif choice == 'report':
        printer.report()
        money_machine.report()
    else:
        station = stations.find_station(choice)
        if station is None:
            print("Wrong Input")
        else:
            if printer.is_resources_sufficient and money_machine.make_payment(station.cost):
                printer.print_ticket(station)