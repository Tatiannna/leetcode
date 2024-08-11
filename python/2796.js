

// 2796. Repeat String

// https://leetcode.com/problems/repeat-string/description/

/**
 * @param {number} times
 * @return {string}
 */
String.prototype.replicate = function(times) {

    let i = 1

    let res = this

    //return this * times
    while (i < times){
        res += this
        i++
    }


    return res
}