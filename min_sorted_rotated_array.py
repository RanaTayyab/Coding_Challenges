

def findMin(nums):
    L = 0

    R = len(nums) - 1

    min_number_so_far = float('inf')

    if nums[L] <= nums[R]:  # for properly sorted array check
        return nums[L]

    while L <= R:  # if it has been rotated then

        M = L + ((R - L) // 2)

        min_number_so_far = nums[M]

        if nums[M] >= nums[L]:  # search on right

            L = M + 1

        else:  # search left

            R = M - 1

        if nums[L] <= nums[R]:  # at any point in time if left number becomes less than right that means we came to fully proper sorted array
            min_number_so_far = min(nums[L], min_number_so_far)
            break

    return min_number_so_far


print(findMin([3,4,5,1,2]))