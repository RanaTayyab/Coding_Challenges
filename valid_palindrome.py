
def isPalindrome(s):

    t = ""

    for ch in s:
        if ch.isalnum():
            t += ch


    i = 0

    j = len(t) - 1

    while i < j:

        if not t[i].lower() == t[j].lower():
            return False

        i += 1

        j -= 1

    return True


