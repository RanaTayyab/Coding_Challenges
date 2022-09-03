
def characterReplacement(self, s: str, k: int) -> int:

    hash_char = {}

    l = 0

    r = 0

    longest = 0

    longest_so_far = 0

    while r < len(s):  # for each element in array keep moving right pointer

        if s[r] in hash_char:  # check if character exists at pointer r

            hash_char[s[r]] += 1  # increase its count

        else:
            hash_char[s[r]] = 1  # or insert new character

        count_of_max_char = max(hash_char.values())  # get max count from characters

        window_length = r - l + 1  # current window length to consider

        if window_length - count_of_max_char <= k:  # if we have enough replacements so far in                                                                   our current window size

            longest_so_far += 1  # increase the long we have so far

            longest = max(longest, longest_so_far)  # update long with Max

        else:

            hash_char[s[
                l]] -= 1  # if condition is not satisfied, move left                               pointer and decrement count of that variable where left pointer was pointing

            l += 1

        r += 1

    return longest
