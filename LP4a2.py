#merge sort 
def merge_sort(arr):#{
 if len(arr) > 1:#{
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):#{
         if left[i] < right[j]:#{
            arr[k] = left[i]
            i += 1 #}
         else:#{
            arr[k] = right[j]
            j += 1 #}
         k += 1 
      #}
    while i < len(left):#{
         arr[k] = left[i]
         i += 1
         k += 1 #}
    while j < len(right):#{
         arr[k] = right[j]
         j += 1
         k += 1 #}
   #}end of if
#}end of function
arr = input("Enter a list of numbers separated by commas: ").split(",")
arr = [int(x) for x in arr]
print("Original list:", arr)
merge_sort(arr)
print("Sorted list:", arr)