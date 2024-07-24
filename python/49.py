# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {} # key: tuple constructed from above dictionary, values words that have the same. Return values() from this

        count = [0] * 26


        # for word in strs:
        #     h = {}
        #     for char in word:
        #         if char not in h:
        #             h[char] = 1
        #         else:
        #             h[char] +=1
        #     tuple_key = tuple(sorted(h.items()))

        #     if tuple_key not in result: # if we have NOT seen this dictionary yet, it goes in a new bucket
        #         result[tuple_key] = [word]
        #     else:                # if we have  seen this dictionary yet, it goes in an existing bucket
        #         result[tuple_key].append(word)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in result:
                result[key] = [word]
            else:
                result[key].append(word)

        return result.values()