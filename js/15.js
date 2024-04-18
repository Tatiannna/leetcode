// 15. 3Sum


// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
// i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.


/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    
    let set = new Set();
    let low = 0;
    let high = nums.length -1;
    let mid = 1;
    
    nums.sort((a,b) => a-b)
    
    while(low < nums.length -3){
        if(nums[low] + nums[mid] + nums[high] === 0){
            set.add([nums[low], nums[mid], nums[high]])
        }else if(nums[low] + nums[mid] + nums[high] > 0){
            high--;
        }else{
            mid++;
        }
        
        if(mid >= high){
            low++
            high = nums.length - 1
            mid = low+1
        }
    }
    
    set.add([1,2])
    return Array.from(set);
};