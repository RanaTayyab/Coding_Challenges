
def maxArea(height):

    maximum_area = - float('inf')

    for i in range(len(height)):
        for j in range( i +1, len(height)):

            spill_over_height = min(height[i], height[j])           # minimum height of two because it should not spill over water

            width = j - i                         # width of two

            area = spill_over_height * width

            maximum_area = max(maximum_area, area)

    return maximum_area



def maxArea_optimized(height):

    maximum_area = - float('inf')

    l = 0

    r = len(height) - 1

    while l <= r:

        width = r - l           # Two pointers

        spill_over_height = min(height[l], height[r])

        area = spill_over_height * width

        maximum_area = max(maximum_area, area)

        if height[l] <= height[r]:
            l += 1

        else:
            r -= 1

    return maximum_area




