# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = ['']
        ans = []

        keys = { 2: ['a', 'b', 'c'], 
                 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 
                 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 
                 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 
                 9: ['w', 'x', 'y', 'z']}

        for digit in digits: 
                for letter in keys[int(digit)]:
                    for i in range(len(combinations)):
                        combinations[i] += letter
                        combinations.append(combinations[i])
                        if len(combinations[i]) == len(digits):
                            ans.append(combinations[i])
        return ans