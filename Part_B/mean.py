
import math

# Read N numbers
N = int(input("Enter the number of values: "))
numbers = []

for i in range(N):
    num = float(input(f"Enter value {i+1}: "))
    numbers.append(num)

# Calculate mean
mean = sum(numbers) / N

# Calculate variance
variance = sum((x - mean) ** 2 for x in numbers) / N

# Calculate standard deviation
std_deviation = math.sqrt(variance)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)