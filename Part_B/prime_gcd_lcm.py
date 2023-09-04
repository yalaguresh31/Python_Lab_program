import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

while True:
    print("\nMenu:")
    print("1. Check if a number is prime")
    print("2. Find GCD and LCM of two numbers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(num, "is prime")
        else:
            print(num, "is not prime")
    elif choice == 2:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("GCD:", gcd(num1, num2))
        print("LCM:", lcm(num1, num2))
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")