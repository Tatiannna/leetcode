// 1282. Group the People Given the Group Size They Belong To

// There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

// You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

// Return a list of groups such that each person i is in a group of size groupSizes[i].

// Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.


// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/


/**
 * @param {number[]} groupSizes
 * @return {number[][]}
 */
var groupThePeople = function(groupSizes) {
    let ans = [];
    let map = {};
    
    for (let i = 0; i < groupSizes.length; i++){
        if (map[groupSizes[i]] === undefined){
            ans.push([i]);
            map[groupSizes[i]] = ans.length - 1;
        }else{
            ans[map[groupSizes[i]]].push(i)
        }
        if (ans[map[groupSizes[i]]].length === groupSizes[i]) map[groupSizes[i]] = undefined
    }
    return ans;
};