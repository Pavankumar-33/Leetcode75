
# Code
# Testcase
# Testcase
# Test Result
# 643. Maximum Average Subarray I
# Easy
# Topics
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum1 = 0.0
        for i in range(0, k):
            sum1 += nums[i]

        max_sum = sum1
        start = 0
        end = k
        while end < len(nums):
            sum1 -= nums[start]
            start += 1

            sum1 += nums[end]
            end += 1

            max_sum = max(max_sum, sum1)

        return (max_sum/k)