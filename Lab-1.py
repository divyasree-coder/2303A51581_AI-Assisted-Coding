#write a program to check whether a given number is prime or not without using functions
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#  optimize the above code 
num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
