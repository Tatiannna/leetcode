// 2418. Sort the People

// You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

// For each index i, names[i] and heights[i] denote the name and height of the ith person.

// Return names sorted in descending order by the people's heights.

// https://leetcode.com/problems/sort-the-people/



/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    let map = {}
    
    for(let i = 0; i < heights.length; i++){
        map[heights[i]] = names[i]
    }
    
    let sortedHeights = Object.keys(map).sort((a,b) => b-a)
    let ans = []
    
    for(let i = 0; i < sortedHeights.length; i++){
        ans.push(map[sortedHeights[i]])
    }
    
    return ans
};