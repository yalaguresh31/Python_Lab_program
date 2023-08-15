# Defined as a function F as Fn = Fn-1 + Fn-2. Write a Python program which accepts a value for N (where N >0) as input and pass this value to the function. Display suitable error message if the condition for input value is not followed.
# Function for nth Fibonacci number
def Fibonacci(n):
        if n == 1:
                return 0
        elif n == 2:
                return 1
        else:
                return Fibonacci(n - 1) + Fibonacci(n - 2)



N = int(input("Enter a value of N : "))
if N<=0:
        print("Invalid Input")
else:
        print("Fibonacci series : ")
        for i in range(1, N+1):
           print(Fibonacci(i), end=" ")
       