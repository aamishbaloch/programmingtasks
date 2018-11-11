def smallest_positive_integer(A):
    for num in range(1, 10000):
        if num not in A:
            return num

    return -1


if __name__ == '__main__':
    data = [1, 4, 3, 9, 8]
    result = smallest_positive_integer(data)
    print(result)
