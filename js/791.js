// 791. Custom Sort String

// You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

// Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

// Return any permutation of s that satisfies this property.


/**
 * @param {string} order
 * @param {string} s
 * @return {string}
 */
var customSortString = function(order, s) {
    let ans = ''
    let extra = ''
 
 for(let i = 0; i < order.length; i++){
     while(s.includes(order[i])){
         ans += order[i]
         s = s.replace(order[i],'')
     }
 }
 
 return ans + s
};