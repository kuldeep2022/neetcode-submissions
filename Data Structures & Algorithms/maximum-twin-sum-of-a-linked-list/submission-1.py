# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now Slow should be second half of the linkedlist

        # Reverse the second half
        prev = None
        curr = slow
       
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        evenSum, oddSum = 0,0
        i = 0

        nhead = prev
        start = head
        res = 0
        while nhead:
            res = max(start.val + nhead.val,res)
            start = start.next
            nhead = nhead.next
            i+=1

        return res
        