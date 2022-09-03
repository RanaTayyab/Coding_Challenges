


def missing_number_through_sorting(arr):   # NLogN
    arr.sort()
    print(arr)

    i = 1
    while i < len(arr):
        if abs(arr[i - 1] - arr[i]) != 1:    # after sorting the array, if difference isn't = 1,
                                            # then add 1 to previous number and return it = missing number
            return arr[i - 1] + 1
        i += 1


def missing_number_through_max_min(arr):

    max_element = len(arr)                   # can take as max of array or length of array

    theoretic_sum = int(((max_element) * (max_element + 1)) / 2)     # (N) * (N+1) / 2

    arr_sum = sum(arr)                                # array sum

    missing_element = theoretic_sum - arr_sum            # their difference is missing number

    if missing_element:
        return int(missing_element)
    else:
        return 0


def getMissingNo_XOR(arr):

    x1 = arr[0]
    x2 = 1

    for i in range(1, len(arr)):
        x1 = x1 ^ arr[i]

    for i in range(2, len(arr) + 2):
        x2 = x2 ^ i

    return x1 ^ x2


def getMissingNo_Overflow(arr):
    i = 0 # start with next elements
    total = 1 # because arrays are starting from 1

    for i in range(2, len(arr) + 2):
        total += i
        total -= arr[i - 2] # subtract from starting indexes
    return total


if __name__ == '__main__':
    arr = [4,1,2,7,6,3]
    #print(missing_number_through_sorting(arr))

    # print(missing_number_through_max_min(arr))

   # print(getMissingNo_XOR(arr))

    print(getMissingNo_Overflow(arr))