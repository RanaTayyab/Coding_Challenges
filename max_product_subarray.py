

def maxProduct(nums):
    maxProductSoFar = nums[0]
    minProductSoFar = nums[0]

    maxProd = nums[0]

    for i in range(1, len(nums)):
        # keeping one max for one iteration, it should not change

        temp_max = max(nums[i], maxProductSoFar * nums[i], minProductSoFar * nums[i])

        minProductSoFar = min(nums[i], maxProductSoFar * nums[i], minProductSoFar * nums[i])

        maxProductSoFar = temp_max

        maxProd = max(maxProd, maxProductSoFar)

    return maxProd

