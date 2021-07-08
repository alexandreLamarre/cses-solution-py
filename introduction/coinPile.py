'''
You have two coin piles containing a and b coins. On each move, you can either remove one coin from the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.

Your task is to efficiently find out if you can empty both the piles.

Input

The first input line has an integer t: the number of tests.

After this, there are t lines, each of which has two integers a and b: the numbers of coins in the piles.

Output

For each test, print "YES" if you can empty the piles and "NO" otherwise.

Constraints
1≤t≤105
0≤a,b≤109
Example

Input:
3
2 1
2 2
3 3

Output:
YES
NO
YES
'''

n = int(input())

for i in range(n):
    ab = input()
    a,b = ab.split()
    a,b = int(a), int(b)
    a , b = (a,b) if a > b else (b,a)
    res = "NO"
    if a==0 and b ==0:
        res ="YES"
    elif a > 2*b :
        res = "NO"
    else:
        check = a -b
        if check% 4 == 2 or check%4 == 1:
            res = "YES"
    print(res)
