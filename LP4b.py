# 4)B) Write a program to convert roman numbers in to integer values using  dictionaries.
def roman_to_int(s):
 roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
 res = 0
 prev = 0
 for i in range(len(s)-1, -1, -1):
    curr = roman_dict[s[i]]
    if curr < prev:
        res = res - curr
    else:
        res = res + curr
        prev = curr
 return res
s = input("Enter a Roman numeral: ")
print("The integer value of", s, "is:", roman_to_int(s))