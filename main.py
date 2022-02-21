from art import car
from wash_pass import WashPass
import os
from datetime import *
from dateutil import parser


wash_pass = WashPass()

os.system('clear')
print('##############################################################')
print('#                                                            #')
print('#                WELCOME TO THE CAR WASH                     #')
print('#                                                            #')
print('##############################################################\n')
print(car)

car_wash_price = input("Enter the price for car wash pass: ")
wash_pass.set_carwash_price(car_wash_price)

members = int(input("\nEnter total no of members: "))

for i in range(1,members + 1):
    member_name = input(f"\nEnter the name of member {i}: ")
    wash_pass.set_member(member_name)

wash_pass.get_members()

start_date = parser.parse(input("\nPlease enter the start date for the pass(MM/DD/yyyy): "))
wash_pass.set_pass_startend_dates(start_date)

wash_pass.print_member_days()
