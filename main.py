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

wash_pass.print_carwash_price()
wash_pass.set_members(5)
start_date = parser.parse(input("Please enter the start date for the pass(MM/DD/yyyy)"))
wash_pass.set_pass_startend_dates(start_date)
