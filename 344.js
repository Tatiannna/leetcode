// Write a function that reverses a string. The input string is given as an array of characters s.

// You must do this by modifying the input array in-place with O(1) extra memory.


/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    
    // abcd
    for (let i = 0; i < Math.floor(s.length/2); i++){
        let temp = s[i];
        s[i] = s[s.length-1-i];
        s[s.length-1-i] = temp;
    }
    
    //return s;
};