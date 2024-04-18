// 2864. Maximum Odd Binary Number

// You are given a binary string s that contains at least one '1'.

// You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

// Return a string representing the maximum odd binary number that can be created from the given combination.

// Note that the resulting string can have leading zeros.

// https://leetcode.com/problems/maximum-odd-binary-number/


/**
 * @param {string} s
 * @return {string}
 */
var maximumOddBinaryNumber = function(s) {
    let count = 0;
    let ans = '';
    
    for(let i = 0; i < s.length; i++){
        if(s[i] === '1') count++;
    }
    
    let zeroes = s.length - count;  
    
    for(let i = 0; i < count-1; i++){
        ans += '1'
    }
    
    for(let i = 0; i < zeroes; i++){
        ans += '0'
    }
    
    ans += '1'
    
    return ans
};