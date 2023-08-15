# 5)B) Develop a python program that could search the text in a file for phone numbers (+919900889977) and email addresses (sample@gmail.com).
import re
def find_phone_numbers_and_emails(filename):
    with open(filename, 'r') as file:
        text = file.read() 
    phone = re.findall(r'\+\d{12}', text)
    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
    return phone, email

filename = 'Files.txt'
phone_numbers, email_addresses = find_phone_numbers_and_emails(filename)
# Print the results
print('Phone numbers:') 
for number in phone_numbers:
    print(number)
print('\nEmail addresses:') 
for email in email_addresses: 
    print (email)
