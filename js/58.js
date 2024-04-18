// 58. Length of Last Word

// Given a string s consisting of words and spaces, return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.

// https://leetcode.com/problems/length-of-last-word/

/**
 * @param {string} s
 * @return {number}
 */

var lengthOfLastWord = function(s) {
    let arr = s.trim().split(' ')

    
    return arr[arr.length-1].length
};