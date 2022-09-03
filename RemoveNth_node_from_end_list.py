
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd( head, n):


    dummy = ListNode();        # inserting a new dummy node in start,
    dummy.next = head;         # attaching dummy before head

    left = dummy               # starting left and right both with dummy

    right = dummy

    counter = n


    while right:

        if counter >= 0:            # move the right pointer counter times first, then start moving
            # left pointer from start and then keep moving right and left pointer step by step

            right = right.next

        else:

            right = right.next

            left = left.next


        counter-=1


    left.next = left.next.next      # at the end remove the element simply

    return dummy.next