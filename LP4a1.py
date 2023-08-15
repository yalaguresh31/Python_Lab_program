# Aim: Discuss different collections like list, tuple and dictionary
# 4)A) Write a python program to implement insertion sort and merge sort using 
# lists
def insertion_sort(arr):#end of function
   for i in range(1, len(arr)):#start for loop
      key = arr[i]
      j = i-1
      while (j>=0) and (arr[j] > key):#start while loop
         arr[j+1] = arr[j]
         j -=1 #end of while loop
      arr[j+1] = key
   #end of for loop
#end of function 

arr = input("Enter a list of numbers separated by commas: ").split(",")
arr = [int(x) for x in arr]
print("Original list:", arr)
insertion_sort(arr)
print("Sorted list:", arr)

