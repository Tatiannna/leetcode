// 1460. Make Two Arrays Equal by Reversing Subarrays

// You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

// Return true if you can make arr equal to target or false otherwise.


// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/


/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function(target, arr) {
    target.sort((a, b) => a - b)
    arr.sort((a, b) => a - b)

    console.log(target)
    
    for(let i = 0; i < target.length; i++){
        if(arr[i] !== target[i]) return false
    }
    
    return true
};