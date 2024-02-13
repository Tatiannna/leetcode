// https://leetcode.com/problems/is-subsequence/


// 392. Is Subsequence

// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

// A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let j = 0;
    let i = 0;

    while(j < t.length){
        if(s[i] !== t[j]) j++;
        else{
            j++;
            i++;
        }
    }
    
    if( i === s.length) return true;
    else return false;
};