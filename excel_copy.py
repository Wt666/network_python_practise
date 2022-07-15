# import math
# from re import M
# from typing_extensions import runtime

# from fitz.fitz import PDF_ANNOT_PRINTER_MARK
# # for i in range(-100,10000):
# #     x=int(math.sqrt(i+100))
# #     y=int(math.sqrt(i+268))
# #     if (pow(x,2) == i+100) and (pow(y,2) == i+268):
# #         print(i)
# # # import math
# # #
# # # a=math.sqrt(100)
# # # print(a)
# # # print(isinstance(a,int))
# #
# # print(math.sqrt(101))
# sum = 0
# for i in range(0, 101):
#     sum += i
# print(sum)
# # class Solution(object):
# #     def isHappy(self, n):
# #         """
# #         :type n: int
# #         :rtype: bool
# #         """
# #         l = [n]
# #         while True:
# #             temp = 0
# #             while(n > 0):
# #                 temp += (n % 10) ** 2
# #                 n /= 10
# #
# #             n = temp
# #             if n == 1:
# #                 return True
# #             elif n in l :
# #                 return False
# #             else:
# #                 l.append(n)
# # x=Solution(19)
# # x.isHappy(19)
# a = 2.5345345345
# print(int(a))
# import math

# print(int(math.log(100, 10)))

# import numpy as np

# p1 = np.array([3, 4])
# p2 = np.array([4, 3])
# p3 = p2 - p1
# print(p3[0])
# print(p3[1])
# p4 = math.hypot(p3[0], p3[1])
# print(p4)
# print(math.hypot(12, 14))
# print(np.array([2, 3, 3, 3, 3, 3, 3, 3.55]))
# age = 11
# name = 'WT'
# print(f"my name is {name}, age is {age}")
# f = 2.222222
# ff = 1000000000
# print('{:.2f}'.format(f))
# print('{:,}'.format(ff))
# s1 = 'Python啦啦啦'
# print(s1.encode(encoding='utf-8'))
# print(s1.isalpha())
# print(s1.count('啦'))
# print([1, 2, 3] + [1, 2, 3, 4] * 2)
# a = [4, 6, 2, 7, 2, 3, 88, 1, 9999, 4]
# b = ['aaa', 'kkkk']
# a.sort()
# b.extend(a)
# print(b)
# print(a)
# print(a[::2])
# for i in range(len(a)):
#     print(a[i])
# print(b[e] for e in [1])
# # print(runtime)
# list = [x**2 + y for x in range(5) for y in range(4, 7)]
# print(list)

# my_dict8 = {'name': 'John', 'age': 25 , 1: [2, 4, 3]}
# my_dict8['name']='WT'
# del my_dict8['age']
# print(my_dict8)
# print(len(my_dict8))
# print(my_dict8.keys())
# print(my_dict8.items())

# seq = ['name', 'age', 'city']
# value = ['Lemon', 18, 'cs']

# my_dict9 = dict.fromkeys(seq, value)
# my_dict10 = dict(zip(seq, value))
# print(my_dict9)
# print(my_dict10)

# strings=("lemon",'lemon','lemon','wt','wt','wt','wt','yyy')
# counts={}
# for kw in strings:
#     counts[kw]=counts.setdefault(kw,0)+1
# print(counts)

a = ['name', 'age', 'class']
b = ['wt', 19, 'first']
my_dic1 = {k: v for (k, v) in zip(a, b)}
print(my_dic1)
x = {'a': 1, 'b': 2}
y = {'b': 4, 'c': 5}
c = {'a': 2, 'e': 44}


def merge(x, y):
    x.update(y)
    return x


print(merge(x, y))
print({**x, **y})


def mutimerge(*dict_args):
    z = {}
    for i in dict_args:
        z.update(i)
    return z
print(mutimerge(x,y,c))

from email import message
import pprint

from nbformat import current_nbformat
from pyrsistent import rex

menu = {'dinner':{'chicken':'good','beef':'average',
                  'vegetarian':{'tofu':'good',
                                'salad':{'caeser':'bad',
                                            'italian':'average'}},
                  'pork':'bad'}}
pprint.pprint(menu)
'''
message=input("hello,put your name: ")
print(f"\n Hello "+message)
age=input("How old are you?")
print(age)
age=int(age)
print(age>=18)
'''
current_number = 0
while current_number <10:
    print(current_number)
    current_number+=1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program"
# message=""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
'''
active =True
while active:
    message=input(prompt)
    if message == 'quit':
        active=False
    else:
        print(message)

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I love {city.title()} very much!")
'''
number = 0
while number <50:
    number +=1
    if number % 2 ==1:
        continue
    print(number)

unverified_person=['rex','wang','tong']
verified_persons=[]
while unverified_person:
    verified_person=unverified_person.pop()
    verified_persons.append(verified_person.title())
for person in verified_persons:
    print(f"Verified person: "+person)

pets=['dog','cat','snake','cat','fish','goldfish','rabbit']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
'''
responses={}
polling_active=True
while polling_active:
    name=input("\nWhat's your name?")
    response=input("Which mountain would you like to climb someday?")
    responses[name]=response #store the response in the dictionary.
    repeat=input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active=False
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
print(responses)
'''

'''
def greet_user(username):
    print(f"Hello {username.title()}")
greet_user('rex')

def division(a,b):
    print(a/b)
division(b=3,a=9)
division(3,9)

def build_person(first_name,last_name,age=None):
    # fullname=f"{first_name} {last_name}"
    person={"first": first_name,"last": last_name}
    if age:
        person['age']=age
    return person
print(build_person('Rex','WANG',age=22))
'''


'''
def fullname(firstname,lastname):
    full_name=f"{firstname} {lastname}"
    return full_name.title()
while True:
    print("What is your name?")
    print(("enter 'q' to break"))
    f_name=input("Please input your first name: ")
    if f_name =='q':
        break
    l_name=input("Please input your last name: ")
    if l_name =='q':
        break
    format_name=fullname(f_name,l_name)
    print(f"\nHello, {format_name}!")
'''

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        print(completed_models)

def show_completed_models(completed_models):
    print("\nTHe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs=['Python','Java','C']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

def pizza_mater(*toppings):
    print(toppings)
pizza_mater('tomato','cheese')

def make_pizza(*materials):
    print("\nYou need these toppings:")
    for topping in materials:
        print(f"- {topping}")
make_pizza('egg','meat','cheese')



class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
class Cat:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fight(self):
        print(f"{self.name} was fighting with {my_dog.name}")
my_cat = Cat('Rex',1)
my_cat.fight()

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading = 100

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""

        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""

        # self.odometer_reading = mileage

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("\nYou can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_car=Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())
# my_car.update_odometer(23500)
# my_car.read_odometer()
# my_car.increment_odometer(100)
# my_car.read_odometer()
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        self.battery_size=75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def battery_update(self,size):
        self.battery_size += size

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""

        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery_update(10)
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

# battery_size1=int(input("battery_size="))
battery_size1=75
class Battery:
    # battery_size1 = input("battery_size=")
    def __init__(self,battery_size=battery_size1):
        self.battery_size=battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""

        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class Luxury_Car(Car):  #second Car: Parent Class
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
mybmw=Luxury_Car("BMW","X6",2022)
print(mybmw.get_descriptive_name())
mybmw.battery.describe_battery()
mybmw.battery.get_range()