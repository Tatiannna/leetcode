// 231. Power of Two

// Given an integer n, return true if it is a power of two. Otherwise, return false.

// An integer n is a power of two, if there exists an integer x such that n == 2x.

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    
    for(let i = 0; i <= n; i++){
        if(2**i === n ){
            return true;
        }else if(2 ** i > n){
            return false;
        }
    }
    return false
};