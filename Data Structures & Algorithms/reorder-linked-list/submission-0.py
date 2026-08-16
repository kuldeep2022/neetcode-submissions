# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Mind the middle of the list
        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # We got the second half of the list which will start from slow.next
        second = slow.next
        prev = slow.next = None

        # just reverse the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # After reversing two halfs we can just merge the two list to create the final list as per required
        first,second = head,prev # prev will be the last node in second half in reverse order

        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2
        