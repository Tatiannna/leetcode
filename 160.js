// 160. Intersection of Two Linked Lists


// Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

// For example, the following two linked lists begin to intersect at node c1:


// The test cases are generated such that there are no cycles anywhere in the entire linked structure.

// Note that the linked lists must retain their original structure after the function returns.

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */

 // todo

 var getIntersectionNode = function(headA, headB) {
    let list = {}
    let current = headA;

    while(current){
        list[current.val] = true;
        current = current.next
    }
    console.log(list)

    current = headB;
    while(current){
        if(list[current.val] === true){
            return current;
        }else{
            current = current.next
        }
    }

    return null;
};