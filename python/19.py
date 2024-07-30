

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num_nodes = 1
        curr = head

        if not curr.next:
            return None

        while curr.next:
            curr = curr.next
            num_nodes += 1

        curr = head

        # Traverse to the node BEFORE the one that needs to be skipped. (num_nodes - n + 1) is the node that needs to be skipped
        nthnode = num_nodes - n


        # If very first node needs to be deleted, return head.next
        if nthnode == 0: 
            return head.next
        else:
            count = 1
            while count < nthnode:
                count += 1
                curr = curr.next

            if curr and curr.next: 
                curr.next = curr.next.next
        
        return head