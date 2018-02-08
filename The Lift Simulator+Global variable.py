'''
total = 0 # Global variable as it is accessible in everywhere
def add(a, b):
    total = a + b
    print (total) # As this variable 'total' is inside the function, it's a local variable (as well as a and b) which only exists in a function.

add(3,3)
print (total)

def add2(a,b):
    global total
    total = a + b
    print (total)

add2(4,5)
print (total)

# Scope = visibility of variable (global / local)
'''

lift = 1
def CallLift():
    currentFloor = int(input("Where are you?"))
    global lift
    for x in range (lift, currentFloor + 1):
        print (x)
    lift = currentFloor

def SetDestination():
    floor = int(input("Please select your floor:"))
    global lift
    while True:
        if floor > 10 or floor < 1:
            floor = int(input("Please enter a valid floor."))
        elif lift == floor:
            print ("You are on the floor you want to reach. You are such an idiot!")
            floor = int(input("Please enter a valid floor"))
        elif 1 <= floor <= 10:
            if lift > floor:
                for y in range (floor, lift + 1, -1):
                    print (y)
                lift = floor
            elif lift < floor:
                for z in range (lift, floor + 1):
                    print (z)
                lift = floor
                print ("Get out. Watch your step.")
                break


def MoveUp():
    global lift
    lift += 1

def MoveDown():
    global lift
    lift -= 1

CallLift()
SetDestination()
