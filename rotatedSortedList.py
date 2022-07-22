# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. You can assume that all the numbers in the list are unique.

# Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.

# We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`. 

# "Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.
from jovian.pythondsa import evaluate_test_cases

test0 = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [4,5,6,7,8,1,2,3]
    },
    'output': 5
}

# A list that wasn't rotated at all.
test2 = {
    'input': {
        'nums': [1,2,3,4,5]
    },
    'output': 0
}

# A list that was rotated just once.
test3 = {
    'input': {
        'nums': [5,1,2,3,4]
    },
    'output': 1
}

# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [2,3,4,5,6,7,8,1]
    },
    'output': 7
}

# A list that was rotated n times, where n is the size of the list
test5 = {
    'input': {
        'nums': [1,2,3,4,5,6,7,8]
    },
    'output': 0
}

# An empty list.
test6 = {
    'input': {
        'nums': []
    },
    'output': 0
}

# A list containing just one element.
test7 = {
    'input': {
        'nums': [1]
    },
    'output': 0
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]

def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)
    
    if len(nums) > 1:
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_number = nums[mid]
            
            if mid > 0 and mid_number < nums[mid-1]:
                # The middle position is the answer
                return mid
            elif mid_number < nums[hi-1]:
                # Answer lies in the left half
                hi = mid - 1  
            else:
                # Answer lies in the right half
                lo = mid + 1
    
    return 0


evaluate_test_cases(count_rotations_binary, tests)