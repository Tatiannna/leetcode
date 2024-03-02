// 977. Squares of a Sorted Array

// Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

// https://leetcode.com/problems/squares-of-a-sorted-array/


/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    
    for(let i = 0; i < nums.length; i++){
        nums[i] **= 2
    }
    
    return nums.sort((a,b) => a-b)

};