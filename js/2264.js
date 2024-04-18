// 2264. Largest 3-Same-Digit Number in String

// You are given a string num representing a large integer. An integer is good if it meets the following conditions:

// It is a substring of num with length 3.
// It consists of only one unique digit.
// Return the maximum good integer as a string or an empty string "" if no such integer exists.

// Note:

// A substring is a contiguous sequence of characters within a string.
// There may be leading zeroes in num or a good integer.


/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function(num) {
    let max = -1;
    let start = 0;

    while(start < num.length - 2){
        if(num[start] === num[start+1] && num[start] === num[start+2] && parseInt(num.slice(start, start+3)) > max){
            max = parseInt(num.slice(start, start+3));
        }
        start++;
    }

    if(max === -1) return ''
    else if (max === 0) return '000'
    else return max.toString();
};