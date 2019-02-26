# -*- coding:utf-8 -*-
"""
@author:Zoe
@file:leetcode-120-triangle.py
@time:2019/2/26上午11:14

@ problems:
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

"""


class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        f = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                f[j] = min(f[j], f[j + 1]) + triangle[i][j]
        return f[0]


if __name__ == '__main__':
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    print(Solution().minimumTotal(triangle))

