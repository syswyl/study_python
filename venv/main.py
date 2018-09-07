from first_pra import *
from mycar import Car
# my_dog = Dog("xiaozi", 6)
# print("my dog's age is " + str(my_dog.age))
# my_dog.sit()
# my_dog.roll()
# print(my_dog.__dict__)
# my_car = Car("audi", "ss", 2018)
# print(my_car.full_information())
# my_car.meter = 100
# my_car.get_meter()
# my_car.modify_meter(50)
# print("after modifying the meter")
# print(my_car.__dict__)
# my_ecar = ElectricCar("tesla", "ss", 2019)
# print('the information of my electric car is : ')
# print(my_ecar.__dict__)
# print(my_ecar.full_information())
# my_ecar.battery.describe_battery()
# my_ecar.show_num()

from collections import OrderedDict
favorite_language = OrderedDict()
favorite_language["ss"] = ['python', 'java']
favorite_language["xmh"] = ['java']
favorite_language['tht'] = ['perl']
for name, language in favorite_language.items():
    print(name + "'s favorite language are the followed: ")
    for lan in language:
        print(lan.lower(), end='~')
    print('\n')


