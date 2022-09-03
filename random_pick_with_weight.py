
import random

class Solution:

    def __init__(self, w):

        self.prefix_sum = [w[0]]

        for i in range(1, len(w)):                   # calculating prefix sum only
            self.prefix_sum.append(self.prefix_sum[i - 1] + w[i])

    def pickIndex(self) -> int:

        random_number = self.prefix_sum[-1] * random.random()  # generate random number in prefix sum range by
                                                                    # accessing it's last element

        # now binary search this random_number in prefix_sum array bucket and return index if matched or lower index

        l = 0
        r = len(self.prefix_sum) - 1

        while l < r:

            m = l + (r - l) // 2

            if random_number > self.prefix_sum[m]:
                l = m + 1

            elif random_number < self.prefix_sum[m]:
                r = m

            elif self.prefix_sum[m] == random_number:  # number found
                return m

        return r  # otherwise return L or R as it is probability only
