'''

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

'''


def solution(X, Y, D):
    return (Y-X)/D if (Y-X) % D == 0 else ((Y-X)/D)+1