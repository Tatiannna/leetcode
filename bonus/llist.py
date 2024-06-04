# https://www.youtube.com/watch?v=WwfhLC16bis
# Basic llist implementation

class Node:

    def __init__(self, num):
        self.val = num
        self.next = None

n = Node(5)
m = Node(6)
l = Node(7)

n.next = m
m.next = l


def returnLength(head):

    node = head
    count = 0

    while(node):
        count += 1
        node = node.next
    return count


print(returnLength(n))
