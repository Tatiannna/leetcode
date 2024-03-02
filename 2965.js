// https://leetcode.com/problems/find-missing-and-repeated-values/

// 2965. Find Missing and Repeated Values

// You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

// Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
    let missing;
    let repeated;
    let map = {};
    
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid.length; j++){
            if(map[grid[i][j]] === undefined){
                map[grid[i][j]] = true
            }else{
                repeated = grid[i][j]
            }
        }
    }
    
    for(let i = 1; i <= grid.length ** 2; i++){
        if(map[i] === undefined) missing = i;
    }
    
    return [ repeated, missing]
};