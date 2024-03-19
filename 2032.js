// 2032. Two Out of Three

// Given three integer arrays nums1, nums2, and nums3, return a distinct 
// array containing all the values that are present in at least two out of the three arrays. 
// You may return the values in any order.


/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @return {number[]}
 */
var twoOutOfThree = function(nums1, nums2, nums3) {
    let ans = []
    let set1 = new Set();
    
    for(let i = 0; i < nums1.length; i++){
        set1.add(nums1[i])
    }
    
    for(let i = 0; i < nums2.length; i++){
        if(set1.has(nums2[i])) ans.push(nums2[i])
        else set1.add(nums2[i])
    }
    
    for(let i = 0; i < nums3.length; i++){
        if(set1.has(nums3[i])) ans.push(nums3[i])
    }
    
    console.log(set1)
    return ans;
};