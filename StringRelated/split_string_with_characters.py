'''

Parse all words in a given text

Definition:

Can you please write a function/class in any language which gets a string and returns an array/list of words. The result array should be unique case insensitive.


example input: "How do you do? Do you like coffee? I/like Coffee."

example output: ["How", "do", "you", "like", "coffee", "I"]

'''

import re

def split_string(test_str):

    # rgx = re.compile("\w[\w']*\w|\w") only when you need to seprate ' as well
    rgx = re.compile("\w+")
    splited_string = rgx.findall(test_str)

    return str(splited_string)


if __name__ == '__main__':
    test_str = input("Enter the String")
    result = split_string(test_str)
    print(result)
