def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


looping = True


while looping:
    user = input("Type 'y' if you want to check if the number is prime or type 'n' to exit: ").lower()

    if user == "y":
        numb = int(input("Enter the number you want to check: "))
        output = is_prime(numb)
        if output:
            print(f"{numb} is prime")
        else:
            print(f"{numb} is not prime")
    elif user == "n":
        print("Have a good day!!")
        looping = False
    else:
        print("Wrong Input")
