

def merge_sorted_arrays(arr1, arr2):

    summation_len = len(arr1) + len(arr2)

    final_arr = []

    i = 0
    j = 0
    k = 0
    while k < summation_len:

        if i < len(arr1) and arr1[i] < arr2[j]:
            final_arr.append(arr1[i])
            i+=1
        elif j < len(arr2) and arr1[i] >= arr2[j]:
            final_arr.append(arr2[j])
            j+=1

        k+=1

    return final_arr



if __name__ == '__main__':
    arr1 = [1,5,7,8,12]
    arr2 = [2,3,4,6,9,11,13]

    print(merge_sorted_arrays(arr1,arr2))