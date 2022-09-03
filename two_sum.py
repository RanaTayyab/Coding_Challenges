
def twoSum_better_sol(nums, target):

    hash_map = {}    # I'll keep track of a hash table

    difference = - float('inf')

    for i in range(len(nums)):

        difference = target - nums[i]        # compute difference between value at that index and the
        # target sum and check the difference value, if it is present in the hash table; if yes,
        # then return this index and the index of number stored in hashmap as value when it was
        # previously stored and the number was key

        if difference in hash_map:
            return [i, hash_map[difference]]

        hash_map[nums[i]] = i      # keep updating hash table



    return None, None

# Optimized byt Two passes

def twoSum(nums, target):
    hash_map = {}  # I'll keep track of a hash table

    flag = False

    index1 = - float('inf')
    index2 = - float('inf')
    difference = - float('inf')

    for i in range(len(nums)):

        difference = target - nums[i]  # compute difference between value at index and target sum and check that value,
        # if it is present in the hash table then later on search that value with another loop to find its index,
        # because we know it is present at some index but that index != index of the first found number,
        # and keep storing every iterated element inside this hash table to check on later

        if difference in hash_map:
            flag = True
            index1 = i
            break

        hash_map[nums[i]] = nums[i]  # keep updating hash table

    if flag:

        for i in range(0, len(nums), 1):

            if i != index1 and nums[i] == difference:  # indexes should be different for both
                index2 = i
                return index1, index2

    return None, None


