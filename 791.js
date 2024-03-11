// 791. Custom Sort String

// You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

// Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

// Return any permutation of s that satisfies this property.


/**
 * @param {string} order
 * @param {string} s
 * @return {string}
 */
var customSortString = function(order, s) {
    
    //     let map = {}
           let ans = ''
           let extra = ''
            
        
    //     for(let i = 0; i < s.length; i++){
    //         if (map[s[i]] === undefined) map[s[i]] == 1
    //         else map[s[i]]++
    //     }
        
    //     for(let i = 0; i < order.length; i++){
    //         if()
    //     }
        
        for(let i = 0; i < order.length; i++){
            if(s.includes(order[i])){
                ans += order[i]
                s.replace(order[i],'')
            }
            // extra += order[i]
        }
        console.log(ans, extra)
        return ans + s
        
    };