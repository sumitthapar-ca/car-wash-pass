from datetime import date
from dateutil.relativedelta import *

class WashPass:
    price = 199
    members = 0

    def __init__(self):
        self.price = (.13 * self.price) + self.price 

    def print_carwash_price(self):
        """Print the price of the car wash pass"""
        print(f'The price of the car wash pass is: {self.price}\n')

    def set_members(self, members):
        self.members = members
        print(f'Total number of members in the pass: {self.members}\n')
        print(f'Price per member: {round(self.price / self.members, 2)}\n')
    
    def set_pass_startend_dates(self, start_date):
        """Set Start and End date for the Car wash pass"""
        self.start_date = start_date
        self.end_date = self.start_date + relativedelta(days=+90)
        print(f"Car wash pass starts on {self.start_date.strftime('%b %d %Y')}")
        print(f"Car wash pass ends on {(self.start_date + relativedelta(days=+90)).strftime('%b %d %Y')}")
