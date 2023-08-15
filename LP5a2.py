#with using regular expressions
import re
def isphonenumber_regex(number):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$') 
    return bool(pattern.match(number))

print(isphonenumber_regex('415-555-4242')) # True
print(isphonenumber_regex('415-555-424')) #False 
print(isphonenumber_regex('415-555-42422')) # False 
print(isphonenumber_regex('415-555-4a42')) # False
