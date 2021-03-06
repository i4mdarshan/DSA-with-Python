# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

def search(nums, target):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = lo + (hi-lo)// 2
            mid_number = nums[mid]

            if mid_number == target:
                return mid
            elif mid_number > nums[lo]:
                # since the portions of array are sorted in ascending order, so if the target is GREATER THAN first element and target is LESS than the middle element that means the target lies on the LEFT side from the mid element so my higher index changes to mid element index
                # Otherwise the element lies in the RIGHT side of the array that is the lower index changes to mid + 1 index
                if target >= nums[lo] and target < mid_number:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                # since the portions of array are sorted in ascending order, so if the target is LESS THAN last element and target is GREATER than the middle element that means the target lies on the RIGHT side from the mid element so my LOWER index changes to mid element index + 1
                # Otherwise the element lies in the LEFT side of the array that is the HIGHER index changes to mid index
                if target <= nums[hi-1] and target > mid_number:
                    lo = mid + 1
                else:
                    hi = mid  
        return -1 

print(search([1,3,5],5))