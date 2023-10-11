while True:
    code = str(input())

    if code == "99999":
        break
    
    direction = code[:2]
    steps = code[2:]
    final = ""
    
    if(direction[0] == "0" and direction[1] == "0"):
        final += previous_direction

    elif (int(direction[0]) + int(direction[1])) % 2 == 0:
        final += "right"
        previous_direction = "right"

    else:
        final += "left"
        previous_direction = "left"

    final += " " 
    final += steps

    print(final)

