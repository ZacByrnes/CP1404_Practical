from taxi import Taxi
from unreliable_car import UnreliableCar
from silverservicetaxi import SilverServiceTaxi


def main():
    #Testing Taxi
    test_taxi = Taxi("Prius 1", 100)
    test_taxi.drive(40)
    print(test_taxi)
    test_taxi.start_fare()
    test_taxi.drive(100)
    test_taxi.get_fare()
    print(test_taxi)
    
    #Testing Unreliable_Car
    
    test_unreliable_car = UnreliableCar("Car 1", 30, 50)
    test_unreliable_car.drive(10)
    print(test_unreliable_car)
    test_unreliable_car.drive(10)
    print(test_unreliable_car)
    test_unreliable_car.drive(10)
    print(test_unreliable_car)
    
    #Testing SilverServicesTaxis
    
    test_silvertaxi = SilverServiceTaxi("Hummer", 200, 4.0)
    test_silvertaxi.drive(40)
    print(test_silvertaxi)

main()
