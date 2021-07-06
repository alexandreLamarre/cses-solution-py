'''
Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).

Input

The only input line has a string of length n consisting of characters A–Z.

Output

Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".

Constraints
1≤n≤106
Example

Input:
AAAACACBA

Output:
AACABACAA
'''

from collections import Counter

input_str = input()

c = Counter(input_str)
mostCommon = list(c.most_common())
res = ""
returned = 0
middle = ""
for i,k in enumerate(mostCommon):
    if k[1] % 2 == 1:
        returned += 1
        if returned > 1:
            print("NO SOLUTION")
            break
        middle = k[0]*k[1]
    else:
        insert = k[0]*k[1]
        res = res[:len(res)//2] + insert +res[len(res)//2:]
if returned == 0: print(res)
elif returned == 1: print(res[:len(res)//2]+middle+res[len(res)//2:])
