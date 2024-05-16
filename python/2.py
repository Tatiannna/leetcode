# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = str(l1.val)
        num2 = str(l2.val)
        p1 = l1
        p2 = l2
        
        while(p1.next):
            num1 += str(p1.next.val) 
            p1 = p1.next

        while(p2.next):
            num2 += str(p2.next.val) 
            p2 = p2.next

        sumStr = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        head = ListNode(int(sumStr[0]))
        p3 = head

        for i in range(1, len(sumStr)):
            p3.next = ListNode(int(sumStr[i]))
            p3 = p3.next

        return head