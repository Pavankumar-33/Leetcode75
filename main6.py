# 238. Product of Array Except Self
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        left = [1] * length
        right = [1] * length
        left_prod = 1
        right_prod = 1

        for i in range(1, length):
            left_prod *= nums[i-1]
            left[i] = left_prod

        for i in range(length-2, -1, -1):
            right_prod *= nums[i+1]
            right[i] = right_prod

        res = []
        for i in range(length):
            a = left[i] * right[i]
            res.append(a)

        return res

