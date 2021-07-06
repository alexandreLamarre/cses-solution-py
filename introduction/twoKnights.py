'''
Your task is to count for k=1,2,…,n the number of ways two knights can be placed on a k×k chessboard so that they do not attack each other.

Input

The only input line contains an integer n.

Output

Print n integers: the results.

Constraints
1≤n≤10000
Example

Input:
8

Output:
0
6
28
96
252
550
1056
1848
'''

n = int(input())

for i in range(1,n+1):
    x = i**2
    print(int(x*(x-1)/2 - (4*(i-1)*(i-2))))
