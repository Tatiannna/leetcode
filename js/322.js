// 322. Coin Change

// You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

// Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

// You may assume that you have an infinite number of each kind of coin.




const change = function(amount, coins){
    let count = 0;
    let min = 7777;

    for(let i = 0; i < coins.length; i++){
        // amount is less than coin[i]
        if(amount < coins[i]){
            continue
        }else if (amount % coins[i] === 0){ // coin[i] evenly divides amount
            count += amount / coins[i]
            if (count < min) min = count
        }else{
            // coin[i] divides amount, but there is a remainder
            // increase count
            // reduce amount to its remainder after division by coins[i]
            count += Math.floor(amount / coins[i])
            amount %= coins[i]
        }
        console.log("count: ", count)
    }

    return min;
}

console.log(change(14, [10, 7, 1]))




