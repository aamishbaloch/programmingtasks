'''

Write a function:

def solution(N, A)

that, given an integer N and a non-empty zero-indexed array A consisting of M integers, returns a sequence of integers representing the values of the counters.

'''


def solution(N, A):

    counters = [0]*N
    for x in A:
        if x == N+1:
            counters = [max(counters)]*N
        else:
            counters[x-1] += 1

    return counters