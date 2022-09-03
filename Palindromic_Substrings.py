
def countSubstrings(s):

    # Exact same code as Longest Palindromic substring because we were keeping all palindromes in our
    # map; this time just return the length of map

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

        r = i + 1

        while l >=0 and r < len(s):

            if s[l] == s[r]:

                result[(l ,r)] = r - l

                l -= 1

                r += 1
            else:
                break




    return len(result)         # return total number of palindromes