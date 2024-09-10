# 2807. Insert Greatest Common Divisors in Linked List
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        def get_gcd(num1, num2):
            small = min(num1, num2)
            ans = 1

            for num in range(small, 0, -1):
                if num1 % num == 0 and num2 % num == 0:
                    ans = num
            return ans

        while curr.next:
            gcd = get_gcd(curr.val, curr.next.val)
            node = ListNode(gcd)
            temp = curr.next
            curr.next = node
            node.next = temp
            curr = node

        return head