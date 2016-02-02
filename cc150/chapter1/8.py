'''
1. if a string is rotation of another string

ans:
1. Concatenate string A
2. See if string B is a substring of A
3. Really close to KMP, which use Partial Match Table to determine shift bits,
in this solution, actually use this idea, to see how many same characters between the prefix and suffix
'''