// 2540. Minimum Common Value

// Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

// Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */

var getCommon = function(nums1, nums2) {
    
    nums1.sort((a,b) => a-b)
    nums2.sort((a,b) => a-b)
    
    let set1 = new Set()
    let set2 = new Set()
    
    for(let i = 0; i < nums1.length; i++){
        set1.add(nums1[i])
    }
    
    for(let i = 0; i < nums2.length; i++){
        set2.add(nums2[i])
        if(set1.has(nums2[i])) return nums2[i]
    }
        
    return -1
};