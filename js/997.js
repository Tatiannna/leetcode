


/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    let map = {};
    let trusters = new Set();
    
    for (let i = 0; i < trust.length; i++){
        trusters.add(trust[i][0])
        if (map[trust[i][1]] === undefined){
            map[trust[i][1]] = 1
        } else {
            map[trust[i][1]] += 1;
        }
        if (map[trust[i][1]] === n - 1 && !trusters.has(trust[i][1])){
            return trust[i][1]
        }
        //console.log(trusters)
                //console.log(map)
    }
    
    return -1
};