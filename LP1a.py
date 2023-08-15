# Write a python program to find the best of two test average marks out of three test''s marks accepted from the user.
a = int(input("Enter 1st test marks:"))
b = int(input("Enter 2nd test marks: "))
c = int(input("Enter 3rd test marks: "))

if a<=b and a<=c:
    print(b,c,"is the best of three test marks")
    avg =(b+c)/2
    print("Average of two test marks",b,"and",c,"is",avg)
elif b<=a and b<=c:
    print(a,c,"is the best of three test marks")
    avg =(a+c)/2
    print("Average of two test marks",a,"and",c,"is",avg)
else:
    print(b,a,"is the best of three test marks")
    avg =(b+a)/2
    print("Average of two test marks",b,"and",a,"is",avg)

