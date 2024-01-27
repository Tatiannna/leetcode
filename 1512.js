// Given an array of integers nums, return the number of good pairs.

// A pair (i, j) is called good if nums[i] == nums[j] and i < j.


/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let pairs = {};
    let count = 0;
    
    for(let i = 0; i < nums.length; i++){
        if(!pairs[nums[i]]) pairs[nums[i]] = 1;
        else pairs[nums[i]] += 1;
        count += pairs[nums[i]] -1;
    }
    
    return count;
};