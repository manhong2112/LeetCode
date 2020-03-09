# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        h = head
        b = 0
        while h != None:
            b = (b << 1) + h.val
            h = h.next
        return b
