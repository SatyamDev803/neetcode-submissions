# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1

        head = None
        tail = None

        while list1 and list2:
            if list1.val < list2.val:
                temp = list1.next
                if head is None:
                    head = list1
                    tail = list1
                else:
                    tail.next = list1
                    tail = list1
                list1 = temp
            else:
                temp = list2.next
                if head is None:
                    head = list2
                    tail = list2
                else:
                    tail.next = list2
                    tail = list2
                list2 = temp
                
        if list1:
            tail.next = list1
        else:
           tail.next = list2

        return head
