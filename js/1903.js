// 1903. Largest Odd Number in String

// You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

// A substring is a contiguous sequence of characters within a string.

/**
 * @param {string} num
 * @return {string}
 */
var largestOddNumber = function(num) {
    let max = 0;
    let low = 0;
    let high = num.length-1;

    while(high >= 0){
        while(num[high] % 2 === 0 && high >= low) high--;
        if(parseInt(num[high]) % 2 === 1 && parseInt(num.slice(low, high+1)) > parseInt(max)){
            return num.slice(low, high+1)
        }
    }
    return max ? max : '';
};