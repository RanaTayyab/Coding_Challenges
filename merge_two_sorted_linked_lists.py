
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1,list2):

    result = ListNode()

    if list1 is None:           # if list 1 is NULL, solution is only list 2
        return list2

    if list2 is None:           # if list 2 is NULL, solution is only list 1
        return list1

    if list1.val <= list2.val:     # Make start
        result.val = list1.val
        list1 = list1.next

    else:
        result.val = list2.val
        list2 = list2.next


    head = result               # store head node


    while list1 and list2:      # while both are not null

        if list1.val <= list2.val:          # two pointer if check of lesser number between two

            temp = ListNode(list1.val)      # make a new node with the value

            result.next = temp

            result = result.next            # add to result

            list1 = list1.next              # move forward

        else:
            temp = ListNode(list2.val)      # similar

            result.next = temp

            result = result.next

            list2 = list2.next


    if list1:                           # if list2 had reached NULL, copy rest of the list1
        while list1:
            temp = ListNode(list1.val)

            result.next = temp

            result = result.next
            list1 = list1.next


    if list2:                           # if list1 had reached NULL, copy rest of the list2
        while list2:
            temp = ListNode(list2.val)

            result.next = temp

            result = result.next
            list2 = list2.next

    result.next = None

    return head