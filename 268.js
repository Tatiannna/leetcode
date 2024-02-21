// 268. Missing Number

// Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

// https://leetcode.com/problems/missing-number/

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    
    nums.sort( (a,b) => a - b);
    
    if (nums[0] !== 0) return 0
    else if (nums[nums.length-1] !== nums.length) return nums.length
    else{
        for(let i = 1; i < nums.length; i++){
            if (nums[i] !== i) return nums[i] - 1
        }
    }
};