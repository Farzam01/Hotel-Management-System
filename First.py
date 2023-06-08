from Rooms import room_number,room_type,features
import sys
from Rooms import room
class guest:
    def __init__(self):
        self.name=str(input("Enter Your Name:"))
        self.id=int(input("Enter a specific id:"))
        self.Dob=(input("Enter your birth date : "))
        self.phone_num=(input("Please Enter Your Phone Number : "))
        self.curr_booking=str(input("Do You have any current booking ? "))
        if self.curr_booking=="Yes":
            print("You can only check in for a Single room...")
            sys.exit(guest)
        elif self.curr_booking=="No":
            print("Proceed..")
    def guest_req(self):
        b=str(input("Do You want to see rooms available rooms:"))
        if (b=="Yes"):
            y=room.select_room(self)
        elif (b=="No"):
            sys.exit()
        else:
            print("Proceed..")

class VIP(guest):

    def special_discount(self):
        s=str(input("Are you a VIP guest ? "))
        if s=='Yes':
            room_number = [90, 20, 34, 21, 11, 10, 5, 8, 4]
            room_type = ['double', 'single', 'suite']
            features = ['standard', 'deluxe']
            room_occupied = []
            for b in room_number:
                for i in room_type:
                    for k in features:
                        no = int(input("Select room number from available list : "))
                        a = str(input("Please select a room"))
                        f = str(input("Please select a feature of a room."))
                        no_of_people = int(input("Enter no of guests , limit for guest is 5 !!"))
                        if (no == b) and (a == room_type) and (f == 'standard'):
                            room_occupied.append(no)
                            room_occupied.append(a)
                            room_occupied.append(f)
                            print("You booked a room for with room type and features ", a, f,
                                          "for $35 after discount..")
                            print(room_occupied)
                            break
                        elif (no==b and (a== room_type) and f=='deluxe'):
                            room_occupied.append(no)
                            room_occupied.append(a)
                            room_occupied.append(f)
                            print("You booked a room for with room type and features ", a, f,
                                          "for $55 after discount..")
                            break
                        elif (no !=b) or(a!=room_type)or(f!='deluxe'):
                            print("Selected options are not available.")
                            break








