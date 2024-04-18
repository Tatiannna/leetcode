/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    let drink = numBottles;
    let remaining = numBottles;

    while( remaining > numExchange){
        drink += Math.floor(remaining/numExchange)
        remaining -= Math.floor(remaining/numExchange)

    }

    return drink
};