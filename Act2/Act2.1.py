first_term = int(input("Enter the first no.: "))
second_term = int(input("Enter the second no.: "))

total = 0

for num in range(first_term, second_term+1): 

    total += num

print(f"The sum of all the numbers between {first_term} and {second_term} is {total}")