// 1534. Count Good Triplets

// Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

// A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function(arr, a, b, c) {
    let count = 0
    let i = 0;
    let j = 1;
    let k = 2;

    arr.sort((a,b) => a-b);
    console.log(arr)

    while(k < arr.length){
        // if(Math.abs(arr[i] - arr[j]) <= a && Math.abs(arr[i] - arr[j]) <= b && Math.abs(arr[i] - arr[j]) <= c) count++;
        if(Math.abs(arr[i] - arr[j]) > a) i++;
        else if(Math.abs(arr[j] - arr[k]) > b) j++;
        else if(Math.abs(arr[i] - arr[k]) > c) i++;
        else count++;

        if(i === j) j++;
        if(j === k) k++;
    }
    return count
};