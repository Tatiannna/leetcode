// 2367. Number of Arithmetic Triplets

// You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

// i < j < k,
// nums[j] - nums[i] == diff, and
// nums[k] - nums[j] == diff.
// Return the number of unique arithmetic triplets.

// https://leetcode.com/problems/number-of-arithmetic-triplets/


/**
 * @param {number[]} nums
 * @param {number} diff
 * @return {number}
 */
var arithmeticTriplets = function(nums, diff) {
    let i = 0
    let j = 1
    let k = 2
    let count = 0
    
    while(k < nums.length){
        while(nums[j] - nums[i] < diff && j < nums.length-1){
            j+=1
            k+=1
        }
        
        if(nums[j] - nums[i] > diff){
            i++;
            j = i+1
            k = j+1
            continue
        }
        
        if(nums[j] - nums[i] === diff){
            while(nums[k] - nums[j] < diff && k < nums.length ){
                k+=1
            }
            if(nums[k] - nums[j] === diff){
                count += 1
                i += 1
                j = i + 1
                k = j + 1
                continue
            }
            else if (nums[k] - nums[j] > diff){
                j++;
                k = j +1;
            }
        }
        
            
    }
    
    return count;
};