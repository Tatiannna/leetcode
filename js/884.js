// 884. Uncommon Words from Two Sentences

// A sentence is a string of single-space separated words where each word consists only of lowercase letters.

// A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

// Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

// https://leetcode.com/problems/uncommon-words-from-two-sentences/



/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function(s1, s2) {
    let uncommon = {}
    let ans = []
    
    let str1 = s1.split(' ')
    for(let i = 0; i < str1.length; i++){
        if(uncommon[str1[i]] === undefined) uncommon[str1[i]] = 1
        else uncommon[str1[i]]++;
    }
     
    let str2 = s2.split(' ')
    for(let i = 0; i < str2.length; i++){
        if(uncommon[str2[i]] === undefined) uncommon[str2[i]] = 1
        else uncommon[str2[i]]++;
    }
    
    let keys = Object.keys(uncommon)
    for(let i = 0; i < keys.length;i++){
        if( uncommon[keys[i]] === 1) ans.push(keys[i])
    }
    
    return ans
};