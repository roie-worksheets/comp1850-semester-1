# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.

from itertools import combinations

def isBond(xs):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """
    # return any(a == 0 and b == 0 and c == 7
    #             for i, a in enumerate(xs)
    #             for j, b in enumerate(xs[i + 1:], i + 1)
    #             for c in xs[j + 1:])
    return (0, 0, 7) in combinations(xs, 3)


# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 7, 5]))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False
