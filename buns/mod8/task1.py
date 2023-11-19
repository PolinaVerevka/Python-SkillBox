class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            self._coordinates = value
        else:
            raise ValueError("Coordinates must be a tuple of length 2")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if isinstance(value, int) and value > 0:
            self._speed = value
        else:
            raise ValueError("Speed must be a positive integer")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise ValueError("Brand must be a string")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int) and value > 0:
            self._year = value
        else:
            raise ValueError("Year must be a positive integer")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if isinstance(value, str):
            self._number = value
        else:
            raise ValueError("Number must be a string")

    def __str__(self):
        return f"Transport: Brand={self.brand}, Year={self.year}, Number={self.number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        x, y = self.coordinates
        if pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width:
            return True
        else:
            return False


class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self._passengers_capacity = passengers_capacity
        self._number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, value):
        if isinstance(value, int) and value > 0:
            self._passengers_capacity = value
        else:
            raise ValueError("Passengers capacity must be a positive integer")

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, value):
        if isinstance(value, int) and value >= 0:
            self._number_of_passengers = value
        else:
            raise ValueError("Number of passengers must be a non-negative integer")


class Cargo:
    def __init__(self):
        self._carrying = None

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, value):
        if isinstance(value, int) and value >= 0:
            self._carrying = value
        else:
            raise ValueError("Carrying capacity must be a non-negative integer")


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value >= 0:
            self._height = value
        else:
            raise ValueError("Height must be a non-negative integer")


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number, color, mileage):
        super().__init__(coordinates, speed, brand, year, number)
        self._color = color
        self._mileage = mileage

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            raise ValueError("Color must be a string")

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if isinstance(value, int) and value >= 0:
            self._mileage = value
        else:
            raise ValueError("Mileage must be a non-negative integer")


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, name, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._name = name
        self._port = port

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        if isinstance(value, str):
            self._port = value
        else:
            raise ValueError("Port must be a string")


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
