
from car import Car
from taxi import Taxi
from silverservicetaxi import SilverServiceTaxi

MENU = "(Q) Quit, (C) Choose taxi, (D) drive "


def main():
    total_cost = 0
    taxis = [Taxi("Prius 1", 100), SilverServiceTaxi("Limo 1", 100, 2),
             SilverServiceTaxi("Hummer 1", 200, 4)]
#Copy menu layout from assignment
#Make sure everything is relating to floats not integers
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis available: ")
            Display_Taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "D":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                         trip_cost))
            total_cost += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_cost))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


def Display_Taxis(taxis):

    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))

#Refer to prac_06 with cars and used_cars.
def Start_Testing():
    """Run tests to show workings of Car and Taxi classes."""
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus.odometer)
    print(bus)

    #I will need to loop bus
    distance = int(input("Drive how far? "))
    while distance > 0:
        travelled = bus.drive(distance)
        print("{} travelled {}".format(str(bus), travelled))
        distance = int(input("Drive how far? "))

    Taxi_2 = Taxi("Prius 1", 100)
    print(Taxi_2)
    Taxi_2.drive(25)
    print(Taxi_2, Taxi_2.get_fare())
    Taxi_2.start_fare()
    Taxi_2.drive(40)
    print(Taxi_2, Taxi_2.get_fare())

    SilverTaxi = SilverServiceTaxi("Limo", 100, 2)
    print(SilverTaxi, SilverTaxi.get_fare())
    SilverTaxi.drive(10)
    print(SilverTaxi, SilverTaxi.get_fare())


main()
