#Camel Banana Problem
total=int(input("Enter number of bananas at start: "))
dist=int(input("Enter total distance to be travelled: "))
load_cap=int(input("Enter maximum number of bananas that camel can carry at a time: "))
lost=0
start=total
for i in range(dist):
    while start>0:
        start=start-load_cap
        if start==1:
            lost-=1
        lost+=2
    lost-=1
    start=total-lost
    if start==0:
        break
print("Bananas delivered: ",start)
