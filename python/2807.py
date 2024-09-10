# 2807. Insert Greatest Common Divisors in Linked List
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        def gcd(num1, num2):
            for num in range(min(num1, num2), 0, -1):
                if num1 % num == 0 and num2 % num == 0:
                    return num
            return 1

        while curr.next:
            print(curr.val)
            divisor = gcd(curr.val, curr.next.val)
            node = ListNode(divisor)
            temp = curr.next
            curr.next = node
            node.next = temp
            curr = temp

        return head