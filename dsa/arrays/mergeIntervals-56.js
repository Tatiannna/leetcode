// https://leetcode.com/problems/merge-intervals/
// 56. Merge Intervals
// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */


var merge = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0])
    let stack = [intervals[0]];

    for (let i = 1; i < intervals.length; i++){
        if (intervals[i][0] <= stack[stack.length-1][1] && intervals[i][1] >= stack[stack.length-1][1] ){
            stack[stack.length-1][1] = intervals[i][1]
        }else if (intervals[i][0] > stack[stack.length-1][1]){
            stack.push(intervals[i])
        }
    }       
    
    return stack;
};





