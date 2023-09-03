# 6)A) Write a python program to accept a file name from the user and perform the following operations 
# 1. Display the first N line of the file 
# 2. Find the frequency of occurrence of the word accepted from the user in the file.

file_name = input("Enter the file name: ")
n = int(input("Enter the number of lines to display: "))
word= input("Enter a word to search for: ")
with open(file_name, "r") as f: 
    for i in range(n):
        line = f.readline()
        print(line.strip())
with open(file_name, "r") as f: 
    content = f.read()
    count = content.count(word)
print("The word '{word}' appears {count} times in the file.") #this line problem
