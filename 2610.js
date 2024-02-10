// 2610. Convert an Array Into a 2D Array With Conditions

// You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

// The 2D array should contain only the elements of the array nums.
// Each row in the 2D array contains distinct integers.
// The number of rows in the 2D array should be minimal.
// Return the resulting array. If there are multiple answers, return any of them.

// Note that the 2D array can have a different number of elements on each row.

// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/




/**
 * @param {number[]} nums
 * @return {number[][]}
 */
/**
 * @param {number[]} nums
 * @return {number[][]}
 */

var findMatrix = function(nums) {
    let n = {}
    let ans = [[]]
    
    for(let i = 0; i < nums.length; i++){
        if( n[nums[i]] === undefined){
            ans[0].push(nums[i])
            n[nums[i]] = 1
        }else{
            if (ans.length === n[nums[i]]) ans.push([nums[i]]);
            else ans[n[nums[i]]].push(nums[i])
            n[nums[i]] += 1
        }
    }
    
    return ans;
};







