// 203. Remove Linked List Elements
// Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    let current = head;
    while(head && head.val== val){
        head = head.next;
    }

    while(current){
        if(current.next && current.next.val === val){
            current.next = current.next.next
        }else{
            current = current.next
        }
    }

    return head;
};


