# -*- coding:utf-8 -*-
"""
@author:Zoe
@file:kmp.py
@time:2019/2/20上午9:52
"""


def PTM(pattern):
    """
    最长公共前后缀
    Args:
        pattern: 待查找字串

    Returns:
        子串的最长公共前后缀数组
    """
    n = len(pattern)
    prefix = [0]  # 第一个位置为0
    max_len = 0
    i = 1
    while i < n:

        if pattern[i] == pattern[max_len]:
            max_len += 1
            prefix.append(max_len)
            i += 1
        else:
            if max_len > 0:
                max_len = prefix[max_len - 1]
            else:
                prefix.append(max_len)
                i += 1
    return prefix


def KMP(text, pattern):
    prefix = PTM(pattern)
    prefix = [-1] + prefix[:-1]  # prefix 后移一位

    # KMP 搜索
    m = len(text)
    n = len(pattern)

    # text[i]  length = m
    # pattern [j]  length =n
    i, j = 0, 0
    while i < m:
        if j == n - 1 and text[i] == pattern[j]:  # 找到之后
            print("Found pattern: %s" % (i - j))
            j = prefix[j]
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = prefix[j]
            if j == -1:
                i += 1
                j += 1


if __name__ == '__main__':
    pattern = "ababcabaa"
    text = "abababababcabaaaacba"
    print(KMP(text, pattern))
