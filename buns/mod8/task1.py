class Transport():
    def init(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def str(self):
        return f"Transport: brand - {self.brand}, year - {self.year}, number - {self.number}"

    @property
    def coordinates(self):
        return self.coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self.coordinates = coordinates

    @property
    def speed(self):
        return self.speed

    @speed.setter
    def speed(self, speed):
        self.speed = speed

    @property
    def brand(self):
        return self.brand

    @brand.setter
    def brand(self, brand):
        self.brand = brand

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, year):
        self.year = year

    @property
    def number(self):
        return self.number

    @number.setter
    def number(self, number):
        self.number = number

    def isInArea(self, posx, posy, length, width) -> bool:
        x, y = self.coordinates
        if posx <= x <= posx + length and posy <= y <= posy + width:
            return True
        else:
            return False


class Passenger:
    @property
    def passengerscapacity(self):
        return self.passengerscapacity

    @passengerscapacity.setter
    def passengerscapacity(self, passengerscapacity):
        self.passengerscapacity = passengerscapacity

    @property
    def numberofpassengers(self):
        return self.numberofpassengers

    @numberofpassengers.setter
    def numberofpassengers(self, numberofpassengers):
        self.numberofpassengers = numberofpassengers


class Cargo:
    @property
    def carrying(self):
        return self.carrying

    @carrying.setter
    def carrying(self, carrying):
        self.carrying = carrying


class Plane(Transport):
    def init(self, coordinates, speed, brand, year, number, height):
        super().init(coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self.height = height


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)

class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port

    @property
    def port(self):
        return self.port

    @port.setter
    def port(self, port):
        self.port = port


class Car(Auto):
    pass


class Bus(Auto, Passenger):
    pass


class CargoAuto(Auto, Cargo):
    pass


class Boat(Ship):
    pass


class PassengerShip(Ship, Passenger):
    pass


class CargoShip(Ship, Cargo):
    pass


class Seaplane(Plane, Ship):
    pass