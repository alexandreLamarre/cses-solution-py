'''
Your task is to divide the numbers 1,2,…,n into two sets of equal sum.

Input

The only input line contains an integer n.

Output

Print "YES", if the division is possible, and "NO" otherwise.

After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.

Constraints
1≤n≤106
Example 1

Input:
7

Output:
YES
4
1 2 4 7
3
3 5 6

Example 2

Input:
6

Output:
NO
'''
n = int(input())
if n % 4 == 0:
        set1 = []
        set2 = []
        print("YES")
        maxN = n
        minN = 1
        mid = maxN//4
        for i in range(1, n+1):
            if i <= mid or i > 3*mid:
                set1.append(str(i))
            else:
                set2.append(str(i))
        print(2 * mid)
        print(" ".join(set1))
        print(2 * mid)
        print(" ".join(set2))

elif n % 4 == 3:
    set1 = []
    n1 = 0
    set2 = []
    n2 = 0
    for i in range(3, n+4, 4):
        if i == 3:
            set1.append(str(1))
            set1.append(str(2))
            set2.append(str(3))
        else:
            r =  i - 4
            set1.append(str(r+1))
            set1.append(str(r+4))
            set2.append(str(r+2))
            set2.append(str(r+3))

    print("YES")
    print(len(set1))
    print(" ".join(set1))
    print(len(set2))
    print(" ".join(set2))
else:
    print("NO")
