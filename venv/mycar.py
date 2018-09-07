"""这个专属于车辆的模块"""


class Car:
    num = 0

    def __init__(self, model, name, year):
        self.model = model
        self.name = name
        self.year = year
        self.meter = 10
        Car.num += 1

    def full_information(self):
        fullname = self.model + ' ' + self.name + ' ' + str(self.year)
        return fullname.upper()

    def get_meter(self):
        print("this car's meter is : " + str(self.meter))

    def modify_meter(self, new_meter):
        if new_meter >= self.meter:
            self.meter = new_meter
        else:
            print("you can not modify the meter！")