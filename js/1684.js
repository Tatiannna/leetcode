// 1684. Count the Number of Consistent Strings


// You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

// Return the number of consistent strings in the array words.


// https://leetcode.com/problems/count-the-number-of-consistent-strings/


/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */

var countConsistentStrings = function(allowed, words){
    let count = 0;
    
    for(let i = 0; i < words.length; i++){
        for(let j = 0; j < words[i].length; j++){
            if(!allowed.includes(words[i][j]))break;
            else if(j == words[i].length - 1) count++;
        }
    }
    
    return count;
};