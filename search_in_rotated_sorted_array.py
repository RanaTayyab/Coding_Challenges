
def search(nums, target):

    L = 0

    R = len(nums) - 1


    while L <= R:

        M = L + (( R -L )//2)

        if nums[M] == target:
            return M


        else:

            if nums[M] >= nums[L]:  # if middle is part of left sorted array

                if target > nums[M] or target < nums[L]: # search right

                    L = M + 1
                else:

                    R = M - 1

            else:         # if middle is part of right sorted array

                if target > nums[R] or target < nums[M]:   # search left
                    R = M - 1

                else:
                    L = M + 1


    return -1