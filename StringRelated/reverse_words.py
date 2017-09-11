def reverse_words(string_to_reverse):
    return ' '.join(reversed(string_to_reverse.split(" ")))


def python_split_implementation(string_to_split):
    word = []
    words = []

    for x in string_to_split:
        if not x == " ":
            word.append(x)
        else:
            words.append(''.join(word))
            word = []

    if word:
        words.append(''.join(word))
    return words


def python_reversed_implementation(string_to_reverse):
    reversed_string = ""

    for x in range(len(string_to_reverse)-1, -1, -1):
        reversed_string += string_to_reverse[x]

    return reversed_string


def python_join_implementation(list_to_join):
    return_string = ""
    for x in list_to_join:
        return_string += x
        return_string += " "

    return return_string.rstrip()


def reverse_string(string_to_reverse):
    return string_to_reverse[::-1]