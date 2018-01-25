lunch = ["Potato", "Noodles", "Spaghetti", "Beef", "Rice", "Pad Thai", "Pork"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print (lunch[1]) # Look up an element

'''
When printing "Noodles" from this array in a pseudocode, the code is: print(lunch[2]) 
'''
# Linear Search

date = input("Enter a date.")
for day in range (7):
    if date == days[day]:
        print (lunch[day])
