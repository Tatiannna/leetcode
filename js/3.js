
// 3. Longest Substring Without Repeating Characters

// Given a string s, find the length of the longest substring without repeating characters.

// https://leetcode.com/problems/longest-substring-without-repeating-characters/




/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let chars = {};
    let longest = '';
    let current = '';
    let i = 0;
    let j = i;
    
    
    while (i < s.length){
        j = i;
        while(j < s.length && chars[s[j]] !== 1){
            chars[s[j]] = 1;
            current += s[j];
            j++;
        }
        if (current.length > longest.length) longest = current;
        if (chars[s[j]] === 1){
            //i++;
            current = '';
            chars = {}; 
            //chars[s[i]] = 1;
        }
        i++;
    }
    
    return longest.length;
};