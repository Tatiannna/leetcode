// 2574. Left and Right Sum Differences



/**
 * @param {number[]} nums
 * @return {number[]}
 */



var leftRightDifference = function(nums) {
    let total = 0;
    let current = 0;
    let ans = [];
    let leftSum = 0;
    let currentSum = 0;
    
    for( let i = 0; i < nums.length; i++){
        total += nums[i];
    }
    
    let rightSum = total;

    
    for(let i = 0; i < nums.length; i++){
        rightSum = total - leftSum
        ans.push(Math.abs(leftSum - rightSum));
        leftSum += nums[i]

    }
    
    return ans;
};