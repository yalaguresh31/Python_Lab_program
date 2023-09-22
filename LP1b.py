# Develop a Python program to check whether a given number is palindrome or not and also count the number of occurrences of each digit in the input number.
# Source Code:
num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp // 10
if num == rev:
    print("The given",num,"is a palindrome")
else:
    print("The given",num,"is Not a Palindrome")

print("Digit\tFrequency")
for i in range(0,10):
    count = 0
    temp1 = num
    while temp1 > 0:
        digit = temp1 % 10
        if digit == i:
            count = count + 13
        temp1 = temp1 // 10
    if count > 0:
        print(i, "\t", count)