from Rooms import room,room_type,room_number,features,room_occupied
global available_room
from First import VIP
class Hotel:
    def __init__(self):
        self.hotel_name=str(input("Enter hotel name : "))
        self.city=city=str(input("Enter city : "))
    def check_in(self):
        print("Please Check the available rooms with features.",
              room_number,room_type,features)
    def check_out(self):
        u=str(input("Do you want to issue invoice for your booking :"))

        if (u =='Yes'):

            print("here is your booking receipt for check-out",room_occupied)





