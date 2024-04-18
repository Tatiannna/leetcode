// 169. Majority Element

// Given an array nums of size n, return the majority element.

// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let hash = {}
    let max = nums[0];

    for(let i = 0; i < nums.length; i++){
        if(hash[nums[i]] === undefined){
            hash[nums[i]] = 1;
        }
        else{
            hash[nums[i]]++;
        }
        if(hash[nums[i]] > hash[max]) max = nums[i];
    }

    return max;
};