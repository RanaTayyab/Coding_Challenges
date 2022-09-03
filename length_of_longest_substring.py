
def lengthOfLongestSubstring_set( s: str) -> int:

    charSet = set()

    l = 0
    res = 0

    for r in range(len(s)):

        while s[r] in charSet:

            charSet.remove(s[l])         # this removal is basically helping us iterate left pointer appropriately
                                        # and start from new string which matters

            l += 1


        charSet.add(s[r])

        res = max(res, r - l + 1)

    return res


print(lengthOfLongestSubstring_set("pwwkew"))





def lengthOfLongestSubstring(s: str) -> int:

    hash_map = {}

    result_longest_str = 0

    longest_string_so_far = 0


    if len(s) == 0:
        return 0

    i = 0
    j = 0

    while i < len(s) and j < len(s):

        if s[j] in hash_map:           # if key exists then update the value of left pointer skipping                                                   all duplicates

            i = max( i , hash_map[s[j]] )           # get max index number of that character

        result_longest_str = max (result_longest_str, j - i + 1)       # caculate longest length


        hash_map[s[j]] = j + 1              # keep storing latest index + 1 of that character

        j += 1


    return result_longest_str