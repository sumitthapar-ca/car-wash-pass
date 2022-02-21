from datetime import date
from dateutil.relativedelta import *

class WashPass:
    price = 0
    members = []

    def __init__(self):
        self.price = (.13 * self.price) + self.price 

    def set_carwash_price(self, car_wash_price):
        """Set the price of the car wash pass"""
        self.price = car_wash_price
        # print(f'The price of the car wash pass is: {self.price}\n')

    def set_member(self, member):
        """Set the no of members within the pass"""
        self.members.append(member)
        # print(f'Total number of members in the pass: {self.members}\n')
        # print(f'Price per member: {round(self.price / self.members, 2)}\n')
    
    def get_members(self):
        for x in self.members:
            print(x)

    def set_pass_startend_dates(self, start_date):
        """Set Start and End date for the Car wash pass"""
        self.start_date = start_date
        self.end_date = self.start_date + relativedelta(days=+90)
        print(f"\nCar wash pass starts on {self.start_date.strftime('%b %d %Y')}")
        print(f"Car wash pass ends on {(self.end_date).strftime('%b %d %Y')}")
        print(f"Total no of days: {(self.end_date - self.start_date).days}")
    
    def print_member_days(self):
        days = (self.end_date - self.start_date).days

        x=0
        for i in range(1, days + 1):
            date_user = self.start_date + relativedelta(days=+ (i-1))
            print(f"{date_user.strftime('%b %d %Y')} is for {self.members[x]}")
            x += 1
            if x >= len(self.members):
                x = 0
                 
            

