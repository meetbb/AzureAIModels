"""
QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element 
as a pivot and partitions the given array around the picked pivot by placing the pivot 
in its correct position in the sorted array.
There are mainly 4 steps in the algorithm:
    1. Choose a pivot
    2. Partion the Array
    3. Recursively Call
    4. Base Case
"""
# Create a partition function
def partition(arr, low, high):
    
    #choose the pivot
    pivot = arr[high]
    print("--------------------")
    print(f"Pivot value is: {pivot}")
    
    # index of smaller element and indicates the right position of pivot found so far.
    i = low - 1
    print(f"i value is: {i}")
    
    # traverse arr[low..high] and move all smaller elements to the left side.
    # Elements from low to i are smaller after every iteration.
    print(f"New Array at initial stage is: {arr}")
    for j in range(low, high):
        print(f"    Jth element is: {arr[j]}")
        if arr[j] < pivot:
            i += 1
            print(" Jth elent is less than pivot so swaping")
            swap(arr=arr, i=i, j=j)
        else:
            print(" Jth element is bigger than pivot")
        print(f"Current array is: {arr}")
    
    # move pivot after smaller elements and return its position
    print("Moving pivot")
    print(f"low value is: {i+1}")
    print(f"high value is: {high}")
    swap(arr=arr, i=i+1, j=high)
    print(f"Array after changing pivot: {arr}")
    return i + 1
            
            
# Create a swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
# The QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(arr=arr, low=low, high=high)
        
        # recursion calls for smaller elements and greater or equals elements.
        quickSort(arr=arr, low=low, high=pi - 1)
        quickSort(arr=arr, low=pi+1, high=high)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    
    quickSort(arr=arr, low=0, high=n-1)
    for val in arr:
        print(val, end=" ")