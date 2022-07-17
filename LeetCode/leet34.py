# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

nums = [5,7,7,8,8,10]
target = 8

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        if result == 'left':
            hi = mid - 1
        if result == 'right':
            lo = mid + 1
    return -1


def leftCondition(mid):
    if nums[mid] == target:
        if mid > 0 and nums[mid - 1] == target:
            return 'left'
        return 'found'
    elif target > nums[mid]:
        return 'right'
    else:
        return 'left'
            
def rightCondition(mid):
    if nums[mid] == target:
        if mid < len(nums)-1 and nums[mid + 1] == target:
            return 'right'
        return 'found'
    elif target > nums[mid]:
        return 'right'
    else:
        return 'left'
            
print([binary_search(0,len(nums)-1,leftCondition),binary_search(0,len(nums)-1,rightCondition)])
        
            
        
