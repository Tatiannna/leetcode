// 1716. Calculate Money in Leetcode Bank

// Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

// He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

// Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.


/**
 * @param {number} n
 * @return {number}
 */
var totalMoney = function(n) {
    let weeks = Math.floor(n/7)
    let adder = 0;
    let money = 0;

    for(let i = 1; i <= weeks; i++){
        for(let day = 1; day <= 7; day++){
            money += adder + day;
        }
        adder++;
    }

    for(let i= 1; i <= n % 7; i++){
        money += i + adder
    }
    return money;
};