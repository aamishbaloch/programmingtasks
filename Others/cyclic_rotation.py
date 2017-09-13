'''

Write a function:

def solution(A, K)

that, given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].

'''


def solution(A, K):
    rotate = len(A)-1
    for x in range(K):
        A = A[rotate:] + A[:rotate]
    return A


# This problem can also be solved without any loop.
# Like dividing K with size and moving the index K/Size Remainder Times.
