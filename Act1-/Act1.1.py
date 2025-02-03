#get three numbers from the user

no1 = float(input("Enter first number: "))
no2 = float(input("Enter second number: "))
no3 = float(input("Enter third number: "))

#determine the highest no.
if no1 >= no2:
    if no1 >= no3:
        highest = no1
    else:
        highest = no3

else:
    if no2 >= no3:
        highest = no2
    else:
        highest = no3

print("The highest number is", highest)

#sort to descend order
if no1 >= no2:
    if no1 >= no3:
        if no2 >= no3:
            print(f"Descending order: {no1}, {no2}, {no3}")
        else:
            print(f"Descending order: {no1}, {no3}, {no2}")
    else: 
        print(f"Descending order: {no3}, {no1}, {no2}")

else:
    if no2 >= no3:
        if no1 >= no3:
            print(f"Descending order: {no2}, {no1}, {no3}")
        else:
            print(f"Descending order: {no2}, {no3}, {no1}")
    else:
        print(f"Descending order: {no3}, {no2}, {no1}")