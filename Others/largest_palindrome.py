def is_palindrome(number):
    return str(number) == "".join(reversed(str(number)))


def get_largest_palindrome(number1, number2):
    for x in range(number1, 0, -1):
        for y in range(number2, x-1, -1):
            mul = x*y
            if is_palindrome(mul):
                return mul
    return -1


print(get_largest_palindrome(99, 99))
