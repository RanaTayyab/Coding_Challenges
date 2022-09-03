

def productExceptSelf(nums):
    prefix = [nums[0]]
    postfix = [nums[-1]]

    result = []

    for i in range(1, len(nums)):
        prefix.append(prefix[i - 1] * nums[i])

    print(prefix)

    i = 0
    j = len(nums) - 1

    while j > 0:
        postfix.insert(0, postfix[0] * nums[j - 1])

        j -= 1
        i += 1

    print(postfix)

    result.append(postfix[1])

    i = 2

    while i < len(nums):
        result.append(prefix[i - 2] * postfix[i])

        i += 1

    result.append(prefix[i - 2])

    print(result)

    return result