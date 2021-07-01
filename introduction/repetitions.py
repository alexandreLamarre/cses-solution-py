'''
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints
1≤n≤106
Example

Input:
ATTCGGGA

Output:
3
'''

dna = input()


longest = 1
cur = longest
for i in range(len(dna) -1):
    if(dna[i] == dna[i+1]):
        cur += 1
    else:
        longest = max(cur, longest)
        cur = 1

longest = max(cur, longest)

print(longest)