no = int(input("Enter the no.: "))

if no > 1:
    is_prime = True
    for i in range (2, int(no ** 0.5) + 1):
        if no % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{no} is a prime number")
    else:
        print(f"{no} is not a prime number")
4
