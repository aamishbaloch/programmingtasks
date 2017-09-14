'''

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

'''


def solution(S):
    stack = []

    for x in S:
        if x in ["(", "{", "["]:
            stack.append(x)
        elif x in [")", "}", "]"]:
            if len(stack) > 0:
                temp = stack.pop()
                if x == ")" and not temp == "(":
                    return 0
                if x == "}" and not temp == "{":
                    return 0
                if x == "]" and not temp == "[":
                    return 0
            else:
                return 0
    if len(stack) == 0:
        return 1
    return 0