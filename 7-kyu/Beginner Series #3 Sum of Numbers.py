"""
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)

(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
"""

# My solution
def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        return calculate(a,b)
    else:
        return calculate(b,a)
    
def calculate(start,end):
    res = 0
    for i in range(start,end+1):
        res += i
    return res

# Best one
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))