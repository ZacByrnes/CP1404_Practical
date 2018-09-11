from silverservicetaxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Taxi 1", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()