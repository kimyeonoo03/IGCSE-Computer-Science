lunch = ["Potato", "Noodles", "Spaghetti", "Beef", "Rice", "Pad Thai", "Pork"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
ways = ["Take a pack lunch.", "Go to cafeteria.", "Don't eat it.", "Throw it away.", "Eat little."]

print (lunch[1]) # Look up an element

'''
When printing "Noodles" from this array in a pseudocode, the code is: print(lunch[2]) 
'''
# Linear Search
import random

date = input("Enter a date.")
while True:
    for day in range (7):
        if date == days[day]:
            print (lunch[day])
            how = random.randint(1, 5)
            print ("It is", date,".", "Today's lunch is:", lunch[day], ".", ways[how])
            break
        if date != days[day]:
            print ("That isn't how you write a day! Please try again.")

