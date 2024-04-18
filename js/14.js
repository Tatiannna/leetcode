// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".



/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let longest = strs[0];
    
    for(let i = 1; i < strs.length; i++){
        for (let j = 0; j < longest.length; j++){
            if (longest[j] !== strs[i][j]){
                longest = longest.slice(0,j)
            }
        }
    }
    
    return longest;
};

