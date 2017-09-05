# Program to check if a string is palindrome or not


class StringUtil:

    @staticmethod
    def is_palindrome(test_str):
        length = len(test_str)

        tail = length-1
        for head in range(int(length/2)):
            if not test_str[head] == test_str[tail]:
                return False
            return True


if __name__ == '__main__':
    test_str = input("Enter the String")

    result = StringUtil.is_palindrome(test_str)

    print(result)
