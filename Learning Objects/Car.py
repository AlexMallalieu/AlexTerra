class Car:
    brand = "Ford"
    price = 296000
    color = "red"
    weight = 2998
    gears = 5
    shifting_mechanism = "sequential"
    horsepower = 650
    rpm = 4000
    engine = "2,0L Ecoboost, 4 cylinder"
    turbo = True
    tax = 10

    def __init__(self, price, weight, gears, horsepower, rpm, turbo, shifting_mechanism):
        self.price = price
        self.weight = weight
        self.gears = gears
        self.horsepower = horsepower
        self.rpm = rpm
        self.turbo = turbo
        self.shifting_mechanism = shifting_mechanism


    def torque(self):
        torque = self.horsepower * 5252 / self.rpm
        return torque

    def total_price(self):
        total_price = 