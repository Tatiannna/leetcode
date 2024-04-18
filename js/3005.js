// 3005. Count Elements With Maximum Frequency

// You are given an array nums consisting of positive integers.

// Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

// The frequency of an element is the number of occurrences of that element in the array.


/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    let map = {}
    let max = 0;
    
    for(let i = 0; i < nums.length; i++){
        if(map[nums[i]] === undefined) map[nums[i]] = 1
        else{
            map[nums[i]]++
        }
        if(map[nums[i]] > max) max = map[nums[i]]
    }
    
    let count = 0
    let values = Object.values(map)
    
    for(i = 0; i < values.length; i++){
        if(values[i] === max) count++
    }
        
    
    return count * max
};