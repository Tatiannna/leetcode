// 1480. Running Sum of 1d Array


// Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

// Return the running sum of nums.


// https://leetcode.com/problems/running-sum-of-1d-array/



/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let arr = [];
    let sum = 0;
    
    for( let i = 0; i < nums.length; i++){
        sum += nums[i]
        arr.push(sum)
    }
    
    return arr
};