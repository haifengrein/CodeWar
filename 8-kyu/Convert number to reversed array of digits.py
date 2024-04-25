"""
Convert number to reversed array of digits

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):

35231 => [1,3,2,5,3]
0 => [0]
"""

# my solution
def digitize(n):
    new_list = list(str(n))
    new_list.reverse()
    return [int(char) for char in new_list]

# best solution
def digitize(n):
    return [int(x) for x in str(n)[::-1]]
def digitize(n):
    return map(int, str(n)[::-1])
