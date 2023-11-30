import random


class ParkingLot:
    def __init__(self, sqr_footage, spot_size=(8, 12)):  #taking tuple as input
        self.spot_size = spot_size
        self.total_no_of_spots = sqr_footage // (spot_size[0] * spot_size[1])
        self.parking_lot = [None] * self.total_no_of_spots

    def park_car(self, car, spot):
        if self.parking_lot[spot] is None:
            self.parking_lot[spot] = car
            return True
        else:
            return False


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return "Car with license plate {}".format(self.license_plate)

    def park(self, parking_lot):
        while True:
            spot = random.randint(0, len(parking_lot.parking_lot) - 1)
            if parking_lot.park_car(self, spot):
                break

        print(f"{self} parked successfully in spot {spot}")


def main():
    parking_lot_size = 2000
    car_license_plates = ["shr7842", "prat456", "rath369", "abc1562", "defg909", "qrew789"]

    parking_lot = ParkingLot(parking_lot_size)

    cars = [Car(license_plate) for license_plate in car_license_plates]

    for car in cars:
        if None in parking_lot.parking_lot:
            car.park(parking_lot)
        else:
            break


if __name__ == "__main__":
    main()
