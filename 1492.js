// You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

// Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kthFactor = function(n, k) {
    let numFactors = 0;
    
    for(let i = 1; i <= n; i++){
        if(n % i == 0){
            numFactors++;
            if (numFactors == k) return i;
        }
    }
    
    return -1;
    
};