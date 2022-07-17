# NOTE: Assuming the array is sorted in DESCENDING Order
# Steps for binary search
# Step1: Find the middle element
# Step2: Check if the middle element is EQUAL to the queried element, if YES check if the previous element is same as the middle element if yes then run the search ahain to find the first occurence of the repeated element and then return it else return the middle element directly
# Step3: Check if the middle element is LESS than the queried element if YES then return the list BEFORE the mid element
# Step4: Check if the middle element is GREATER than the queried element if YES then return the list AFTER the mid element.

nums = [8,7,6,5,4,3,2]
query = 3

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def locate_query(nums, query):
    def condition(mid):
        if nums[mid] == query:
            if mid > 0 and nums[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif nums[mid] < query:
            return 'left'
        else:
            return 'right'
    
    return binary_search(0, len(nums) - 1, condition)

print(locate_query(nums,query))