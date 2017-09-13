'''

Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

'''


def solution(A):
    numbers = sorted(A)

    stack = -1
    for x in numbers:
        if stack == -1:
            stack = x
        elif stack == x:
            stack = -1
    return stack
