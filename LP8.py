# 8)A) Write a python program to find the whether the given input is palindrome 
# or not (for both string and integer) using the concept of polymorphism and 
# inheritance.

class Palindrome:
    def is_palindrome(self, input):
        pass
class StringPalindrome(Palindrome):
    def is_palindrome(self, input):
        return input == input[::-1]
class IntegerPalindrome(Palindrome):
    def is_palindrome(self, input):
        return str(input) == str(input)[::-1]

sp = StringPalindrome()
print(sp.is_palindrome("racecar"))
print(sp.is_palindrome("hello")) 

ip = IntegerPalindrome()
print(ip.is_palindrome(12321)) 
print(ip.is_palindrome(12345)) 