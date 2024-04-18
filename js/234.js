// 234. Palindrome Linked List

// Given the head of a singly linked list, return true if it is a 
// palindrome
//  or false otherwise.


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let str = String(head.val)
    
    while(head.next){
        str += String(head.next.val);
        head = head.next
    }
    
    for(let i = str.length-1; i >= 0; i--){
        if (str[i] != str[str.length-i-1]) return false
    }
    
    return true
};

