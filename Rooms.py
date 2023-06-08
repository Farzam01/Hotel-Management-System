global room_type
global features
global room_number
global room_occupied
room_number=[90,20,34,21,11,10,5,8,4]
room_type=['double','single','suite']
features=['standard','deluxe']
room_occupied=[]
class room:
    def __init__(self):
        pass
    def rooms_available(self):
        print("Rooms which are free are as following:",room_number)
    def select_room(self):
        print(room_number)
        print(room_type)
        print(features)
        room_occupied = []
        for b in room_number:
            for i in room_type:
                for k in features:
                    while True:
                        no=int(input("Select room number from available list : "))
                        a = str(input("Please select a room"))
                        f = str(input("Please select a feature of a room."))
                        if (no== b) and (a == room_type ) and (f == 'standard'):
                            room_occupied.append(no)
                            room_occupied.append(a)
                            room_occupied.append(f)
                            print("You booked a room for with room type and features ",a,f,"for $40..")
                            return
                        elif (no==b and (a== room_type) and f=='deluxe'):
                            room_occupied.append(no)
                            room_occupied.append(a)
                            room_occupied.append(f)
                            print("You booked a room for with room type and features ", a, f,"for $60..")
                            return
                        else:
                            break




