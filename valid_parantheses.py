
def isValid(s):

    stack = []


    i = 0

    while i < len(s):

        if s[i] == "(" or s[i] == "{"  or s[i] == "[":

            stack.append(s[i])

        else:

            if len(stack) != 0:

                last_bracket  = stack[-1]

                if (s[i] == ")" and last_bracket == "(") or (s[i] == "}" and last_bracket == "{") or \
                        (s[i] == "]" and last_bracket == "["):

                    stack.pop()

                else:
                    return False

            else:
                return False

        i += 1

    if len(stack) == 0:
        return True
    else:
        return False