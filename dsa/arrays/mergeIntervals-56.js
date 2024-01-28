// https://leetcode.com/problems/merge-intervals/

// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    let ans = [];
    let i = 0;
    
    while( i < intervals.length){
        if (intervals[i][intervals[i].length - 1] < intervals[i+1][0]){
            ans.push(intervals[i])
            i++;
        }else{
            ans.push([intervals[i][0]]);
            while(intervals[i][intervals[i].length - 1] >= intervals[i+1][0]){
                i++;
            }
            ans[ans.length-1].push(intervals[i][0])
        }
        i++;
    }
    return ans;
};