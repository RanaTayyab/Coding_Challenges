

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):


    previous = None        # to make the new end of array at NULL

    current = head        # to start with head


    while current is not None:

        temp = current.next         # storing next link before overriding it by previous link

        current.next = previous     # reversing the link to previous node

        previous = current          # updating pointer previous

        current = temp              # updating pointer previous


    head = previous


    return head



def reverseList_recursion(head):

    def reversing(current, previous):

        if current is None:  # base case
            return previous

        else:
            temp = current.next  # reversing links steps are same
            current.next = previous

            return reversing(temp, current)  # update current and previous through recursion by passing new values

    return reversing(head, None)


