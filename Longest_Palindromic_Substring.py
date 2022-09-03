
def longestPalindrome_expandFromEachCharacter(s):

    l = 0

    r = 0

    result = {}

    for i in range (len(s)):      # the idea is to expand out of each character to opposite sides and
                                # keep matching characters, break when unmatched

        # odd length chunk

        l = i

        r = i

        while l >=0 and r < len(s):         # left pointer goes left and right pointer goes right while
                                            # expanding till strings are matched

            if s[l] == s[r]:

                result[(l ,r)] = r - l       # storing indexes for every palindrome

                l -= 1

                r += 1
            else:
                break


        # repeating same for even length chunk

        l = i

        r = i + 1           # important

        while l >=0 and r < len(s):

            if s[l] == s[r]:

                result[(l ,r)] = r - l

                l -= 1

                r += 1
            else:
                break

    tup = max(result, key=result.get)  # key with max length of palindrome

    t1, t2 = tup

    # print(t1)

    # print(t2)

    return s[t1:t2+1]  # using indexes of max length to return that substring





def longestPalindrome(s):
    # This works

    l = 0  # left pointer

    r = len(s) - 1  # right pointer

    index1 = []  # store left pointer starting index when it matches

    index2 = []  # store right pointer index when it matches with left

    result = {}  # store tuple of L,R

    if len(s) <= 1:  # if length is 0 or 1 then return string itself
        return s

    if len(s) == 2:  # if length is 2 then check if matches then return string otherwise first
        if s[0] == s[1]:
            return s
        else:
            return s[0]

    '''
    "xaabacxcabaaxcabaax"
    '''

    for i in range(len(s)):  # for each element

        l = i  # left at current i value to check for all characters one by one

        r = len(s) - 1  # and keep right pointer at end whenever comes out of 2nd loop

        while l < r:  # like basic palindrome

            if s[l] != s[r]:

                if index2:  # if index2 was filled that means it had matched but came out of
                    # that else; and now r needs to go back at last value of matched

                    r = index2[-1]

                    index1 = []  # as it unmatched so no need to save

                    index2 = []

                    l = i  # keep left pointer at current value of i again to check completely all the
                            # palindromic substrings for that character whenever comes out of 2nd loop

                r -= 1  # keep decrementing R if not matched

            else:

                if s[l] == s[r]:  # if matched

                    index1.append(l)  # 0

                    index2.append(r)  # 13

                    l += 1  # move both

                    r -= 1

        if index1 or index2:  # if something is filled, need tuple result

            result[(index1[0], index2[0])] = index2[0] - index1[0]

    # print(result)                         # returns all the palindromes

    tup = max(result, key=result.get)  # key with max length of palindrome

    t1, t2 = tup

    # print(t1)

    # print(t2)

    return s[t1:t2+1]  # using indexes of max length to return that substring
