from art import car
from car_wash_pass import CarWashPass
import os
from datetime import *
from dateutil import parser


car_wash_pass = CarWashPass()

os.system('clear')
print('##############################################################')
print('#                                                            #')
print('#                WELCOME TO THE CAR WASH                     #')
print('#                                                            #')
print('##############################################################\n')
print(car)

car_wash_price = input("Enter the price for car wash pass: ")
car_wash_pass.set_carwash_price(car_wash_price)

members = int(input("\nEnter total no of members: "))

for i in range(1,members + 1):
    member_name = input(f"\nEnter the name of member {i}: ")
    car_wash_pass.set_member(member_name)

car_wash_pass.get_members()

start_date = parser.parse(input("\nPlease enter the start date for the pass(MM/DD/yyyy): "))
car_wash_pass.set_pass_startend_dates(start_date)

car_wash_pass.print_member_days()
