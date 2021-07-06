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
        set1 = ""
        set2 = ""
        print("YES")
        maxN = n
        minN = 1
        mid = maxN//2
        while(n):
            if n <= mid:
                set2 += " " + str(minN) + " " + str(maxN)
            else:
                set1 += " " + str(minN) + " " + str(maxN)
            n -= 2
            minN += 1
            maxN -= 1
        print(mid)
        print(set1.lstrip())
        print(mid)
        print(set2.lstrip())

elif n % 4 == 3:
    set1 = ""
    n1 = 0
    set2 = ""
    n2 = 0
    for i in range(3, n+4, 4):
        if i == 3:
            set1 = "1 2"
            n1 += 2
            set2 = "3"
            n2 += 1
        else:
            r =  i - 4
            set1 += " " + str(r+1) + " " + str(r+4)
            set2 += " " + str(r+2) + " " + str(r+3)
            n1 += 2
            n2 += 2
    print("YES")
    print(n1)
    print(set1)
    print(n2)
    print(set2)
else:
    print("NO")
