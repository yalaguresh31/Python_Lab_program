# Develop a python program to convert binary to decimal, octal to hexadecimal using functions.
def binary_to_decimal(binary):
    decimal,power = 0,0
    while binary != 0:
        last_digit = binary%10
        decimal = decimal + last_digit*(2**power)
        binary = binary//10
        power += 1
    return decimal

def octal_to_hexadecimal(octal):
    decimal,power = 0,0
    while octal != 0:
        last_digit = octal%10
        decimal = decimal + last_digit*(8**power)
        octal = octal//10
        power += 1
    conversion_table = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    hexadecimal = " "
    while decimal > 0:
        remainder = decimal%16
        if remainder >= 10:
            hexadecimal = conversion_table[remainder] + hexadecimal
        else:
            hexadecimal = str(remainder) + hexadecimal
        decimal = decimal//16
    return hexadecimal

b = int(input("Enter the binary number: "))
print(binary_to_decimal(b))
o = int(input("Enter the octal number: "))
print(octal_to_hexadecimal(o))

