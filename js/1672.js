// https://leetcode.com/problems/richest-customer-wealth/

// You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

// A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.


/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let max = 0;
    
    for (let i = 0; i < accounts.length; i++){
        let rowTotal = 0;
        
        for (let j = 0; j < accounts[i].length; j++){
            rowTotal += accounts[i][j];
        }
        if (rowTotal > max) max = rowTotal;
    }
    
    return max;
};