
// 2744. Find Maximum Number of String Pairs

// You are given a 0-indexed array words consisting of distinct strings.

// The string words[i] can be paired with the string words[j] if:

// The string words[i] is equal to the reversed string of words[j].
// 0 <= i < j < words.length.
// Return the maximum number of pairs that can be formed from the array words.

// Note that each string can belong in at most one pair.


// https://leetcode.com/problems/find-maximum-number-of-string-pairs/




/**
 * @param {string[]} words
 * @return {number}
 */
var maximumNumberOfStringPairs = function(words) {
    let map = {};
    let count = 0;
    
    for (let i = 0; i < words.length; i++){
        if (map[words[i].split('').reverse().join('')] === true ) count++
        if ( map[words[i]] === undefined) map[words[i]] = true
    }
    return count; 
};