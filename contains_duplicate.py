

def containsDuplicate(nums) -> bool:
    s = set(nums)

    # Create a Hash Set, if length != that means it had duplicates in the original array

    if len(nums) != len(s):
        return True

    return False


