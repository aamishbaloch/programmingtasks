# Program to reverse a string without moving special characters


class StringUtil:

    @staticmethod
    def reverse_string(test_str):

        # Returns true if x is an aplhabatic character, false otherwise
        def isAlphabet(x):
            return x.isalpha()

        def swap(a, b):
            return b, a

        length = len(test_str)
        head = 0
        tail = length - 1

        while head < tail:
            if not isAlphabet(test_str[head]):
                head += 1
            elif not isAlphabet(test_str[tail]):
                tail -= 1
            else:
                test_str[head], test_str[tail] = swap(test_str[tail], test_str[head])

        return str(test_str)


if __name__ == '__main__':
    test_str = input("Enter the String")

    result = StringUtil.reverse_string(test_str)

    print(result)
