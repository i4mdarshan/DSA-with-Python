# Note: This algorithm works only if the array is sorted

def binary_search(arr,item):

    # Get Middle element of the array
    mid = len(arr) // 2

    # Check if array exists
    if len(arr) > 0:

        # Check if the item itself is the middle element
        if arr[mid] == item:
            return True

        # Check if the item is less than the middle element and return left side of the array
        if item < arr[mid]:
            return binary_search(arr[:mid],item) 

        # Check if the item is greater than the middle element and return right side of the array
        if item > arr[mid]:
            return binary_search(arr[mid + 1: ],item)
    else:
        return False

    
print(binary_search([10,20,30,40,50,60,70],5))