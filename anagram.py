

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    hash_char = {}

    for char in s:

        if char in hash_char:

            hash_char[char] += 1

        else:

            hash_char[char] = 1

    for char_in_t in t:
        if char_in_t in hash_char:
            hash_char[char_in_t] -= 1
        else:
            return False

    for v in hash_char.values():
        if v != 0:
            return False

    return True