#Vacuum World Problem
cost=0
vac_pos=input("Enter the room (A/B) in which the vacuum cleaner is present: ")
pos_stat=int(input("Enter status of this room: "))
other_stat=int(input("Enter status of the other room: "))
if vac_pos=='A':
    print("Vacuum cleaner is present in room A")
    if pos_stat==1:
        print("Room A is dirty")
        cost+=1
        print("Now cleaned room A")
    else:
        print("Room A is clean")
    if other_stat==1:
        print("Room B is dirty")
        print("Going to room B")
        cost+=1
        print("Vacuum cleaner is now present in room B")
        cost+=1
        print("Now cleaned room B")
    else:
        print("Room B is clean")
        print("No Operation")
else:
    print("Vacuum cleaner is present in room B")
    if pos_stat==1:
        print("Room B is dirty")
        cost+=1
        print("Now cleaned room B")
    else:
        print("Room B is clean")
    if other_stat==1:
        print("Room A is dirty")
        print("Going to room A")
        cost+=1
        print("Vacuum cleaner is now present in room A")
        cost+=1
        print("Now cleaned room A")
    else:
        print("Room A is clean")
        print("No Operation")
print("Goal State Achieved with cost:",cost)
