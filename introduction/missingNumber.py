'''
You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

Input

The first input line contains an integer n.

The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).

Output

Print the missing number.
'''

import sys

n = int(input())
nums = input()

nums = nums.split()
sum = 0
for i in range(len(nums)):
    sum += int(nums[i])

allSum = n*(n+1)/2
print(int(allSum - sum))