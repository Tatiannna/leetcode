// https://leetcode.com/problems/contains-duplicate-ii/

// 219. Contains Duplicate II

// Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    let n = {}
   
   
   for(let i = 0; i < nums.length; i++){
       if (n[nums[i]] === undefined) n[nums[i]] = i
       else{
           if(Math.abs(n[nums[i]] - i) <= k ) return true;
           else n[nums[i]] = i
       }
   }
   
   return false;
};