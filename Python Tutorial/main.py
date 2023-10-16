# Variables
schedule = [] #---> an array (used to store information/variables)
block = 1

# FOR loop
for i in range(4):
    classes = input(f"block {block}:") # grabs user input (the classes they are taking in our context)
    schedule.append(classes) # adds the "classes" user input into the array we made above
    print(schedule) # printing out the result just for us to see
    block += 1 # 

# If, elif, and else statements (checks in subsequential order) 
if "math" in schedule:
    print("you have math!")
elif "chemistry" in schedule:
    print("you have chemistry!")
else:
    print("you DONT have chemistry or math")