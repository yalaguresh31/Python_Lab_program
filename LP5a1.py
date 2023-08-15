# Aim: Demonstration of pattern recognition with and without using regular expressions.
# 5)A) Write a function called isphonenumber() to recognize a pattern 415-555-4242 without using regular expression and also write the code to recognize the same pattern using regular expression.

#Test the isphonenumber() function without using regular expressions
def isphonenumber(number): 
    if len(number) != 12:
        return False
    for i in range(0,3):
        if not number[i].isdecimal():
            return False
    if number[3] != '-':
        return False
    for i in range(4,7):
        if not number[i].isdecimal():
             return False
    if number[7] != "-":
     return False
    for i in range(8, 12):
        if not number[i].isdecimal():
            return False
    return True

print(isphonenumber('415-555-4242')) #true
print(isphonenumber('415-555-424')) # False
print(isphonenumber('415-555-42422')) #False
print(isphonenumber('415-555-4a427')) #False



