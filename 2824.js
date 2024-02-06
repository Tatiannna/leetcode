// 2824. Count Pairs Whose Sum is Less than Target


// Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var countPairs = function(nums, target) {
    let count = 0;
    
    for (let i = 0; i < nums.length; i++){
        for( let j = 0; j < nums.length; j++){
            if(nums[i] + nums[j] < target && i < j) count++
        }
    }
    
    return count;
};