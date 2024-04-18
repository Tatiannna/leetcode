// 1281. Subtract the Product and Sum of Digits of an Integer

// Given an integer number n, return the difference between the product of its digits and the sum of its digits.

// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/



/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let stringNum = String(n);
    let sum = 0;
    let product = 1;
    
    for(let i = 0; i < stringNum.length; i++){
        sum += parseInt(stringNum[i]);
        product *= parseInt(stringNum[i]);
    }
    
    return product - sum;
};