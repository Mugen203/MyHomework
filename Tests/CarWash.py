import time
import datetime
from config import client

#Class to hold customer info

class Customer:
    print("\nWelcome Customer!\n")

    # Had to comment out the constructor because it was not needed

    # def __init__ (self, name, license_no, car_type, car_brand, phone_no, email, twitter):
    #      self.name = name
    #      self.license_no = license_no
    #      self.car_brand = car_brand
    #      self.car_type = car_type
    #      self.phone_no =  phone_no
    #      self.email = email
    #      self.twitter = twitter

    def getInfo(self):
        global customer_info

        self.name = str(input("Please enter your name: "))
        self.license_no = str(input("Please enter your car license number: "))
        self.car_brand = str(input("Please enter your car's brand: "))
        self.car_type = str(input("Please enter your car's type: "))
        self.phone_no = str(input("Please enter your phone number: "))
        self.email = str(input("Please enter your email address: "))
        self.twitter = str(input("Please enter your twitter handle: "))

        customer_info = [self.name, self.license_no, self.car_brand, self.car_type, self.phone_no, self.email, self.twitter]


        #print(customer_info) - Was used to test if the variable customer_info stored the info

        
        return customer_info

        
class Login(Customer):
    def login(self,Customer):
        Customer.getInfo()



class SMS(Customer):
    def send_message(self):
        client.messages.create(
            body= "You will be notified as soon as your car is ready. Thank you for using our service!",
            from_="7753641017",
            to = customer_info[4]
        )





Customer1 = Customer()
Customer1.getInfo()

client1 = SMS()
client1.send_message()