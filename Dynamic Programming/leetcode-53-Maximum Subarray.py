# -*- coding:utf-8 -*-
"""
@author:Zoe
@file:leetcode-53-Maximum Subarray.py
@time:2019/2/26上午11:56

@ problems：
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution(object):
    def maxSubArray(self, arr):
        if not arr:
            return 0
        n = len(arr)
        sub_array = arr[0]
        result = sub_array
        for i in range(1, n):
            if sub_array < 0:
                sub_array = 0
            sub_array += arr[i]
            result = max(result, sub_array)
        return result


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(arr))