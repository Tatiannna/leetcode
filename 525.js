// 525. Contiguous Array

// Given a binary array nums, return the maximum length of a contiguous subarray 
// with an equal number of 0 and 1.



/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
    let left = 0;
    let right = 1;
    let max = right - left + 1;
    let oneCount;
    let zeroCount;
    
    while( right < nums.length){
        if(nums[left] === 0) zeroCount++
        else oneCount++;
        
        if(nums[right] === 0) zeroCount++
        else oneCount++;
        
        if(nums[right+1] + nums[right +2] === 1){
            right += 2;
            max +=2;
        }else{
            
        }   
    }
};