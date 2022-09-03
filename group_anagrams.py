


def groupAnagrams(strs):

    from collections import defaultdict     # it doesn't raise exception for first time

    result = defaultdict(list)             # has to define the type here it's must


    for current_string in strs:

        character_count_arr = [0] * 26       # one index for each character


        for char in current_string:

            index_of_char = ord(char) - ord("a")     # caculated which index to map to, for this character

            character_count_arr[index_of_char] += 1      # how many times it is found and counting that


        char_tup = tuple(character_count_arr)     # making a tuple out of list for making it key

        result[char_tup].append(current_string)    # result{ tuple([]) : []  }



    return result.values()