// 876. Middle of the Linked List

// Given the head of a singly linked list, return the middle node of the linked list.

// If there are two middle nodes, return the second middle node.


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let count = 1;
    let current = head;

    while(current.next){
        count++;
        current = current.next;
    }

    current = head;
    let i = 0;
    while (i < Math.floor(count/2)){
        current = current.next
        i++;
    }

    return current;

}
