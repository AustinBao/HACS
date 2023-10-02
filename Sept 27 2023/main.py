# Variables, loops, arrays, and if-statements 
# schedule = []
# block = 1

# for i in range(4):
#     classes = input(f"block {block}:")
#     schedule.append(classes)
#     print(schedule)
#     block += 1

# if "math" in schedule:
#     print("you have math!")
# elif "chemistry" in schedule:
#     print("you have chemistry!")
# else:
#     print("you DONT have chemistry or math")

schedule = []
block = 1

for i in range(4):
    classes = input(f"block {block}:")
    schedule.append(classes)
    print(schedule)
    block += 1

if "math" in schedule:
    print("you have math!")
elif "chemistry" in schedule:
    print("you have chemistry!")
else:
    print("you DONT have chemistry or math")