
def maxsubarraysum(lst):

    maxSum = - float('inf')
    currSum = - float('inf')

    i = 0
    j = 0

    while i < len(lst):
        currSum = lst[i]
        j = i + 1
        while j < len(lst):
            currSum = currSum + lst[j]
            if maxSum < currSum:
                maxSum = currSum
            j+=1
        i+=1

    print(maxSum)



def max_sub_array_sum_dp(lst):

    sum_so_far = - float('inf')
    sum_at_index = - float('inf')

    i = 1

    sum_so_far = lst[0]

    max_sum = lst[0]

    while i < len(lst):
        sum_so_far += lst[i]  # keep on adding next numbers

        sum_at_that_index = lst[i]   # get number on that index only

        if sum_so_far < sum_at_that_index:       # sum so far gets smaller than sum at that index only
            sum_so_far = sum_at_that_index

        max_sum = max(max_sum, sum_so_far)    # it caters if some old max sum in array was bigger, preserving that

        i+=1

    print(max_sum)



if __name__ == '__main__':
    #lst = [-2,1,-3,4,-1,2,1,-5,4]
    lst  = [5, 4, -1, 7, 8]
    #maxsubarraysum(lst)
    max_sub_array_sum_dp(lst)



