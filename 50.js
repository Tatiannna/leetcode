// Implement pow(x, n), which calculates x raised to the power n (i.e., xn).




/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if (n == 0) return 1
    else if (x == 1) return 1;
    
    let isNeg = n < 0;
    let res = 1;
    
    if(isNeg){
        n *= -1;
    }
    
    for(let i = 0; i < Math.floor(n/2) ; i++){
        res *= x;
    }
    
    if(isNeg) res = 1/res;
    
    
    if (n % 2 !== 0) return (res ** 2) * res;
    else return res ** 2;
    
    
};