# 2085. Count Common Words With One Occurence


# Given two string arrays words1 and words2, return the number of 
# strings that appear exactly once in each of the two arrays.


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        s1 = {}
        s2 = {}
        count = 0

        for word in words1:
            if word not in s1:
                s1[word] = 1
            else:
                s1[word] +=1 
        
        for word in words2:
            if word in s1 and s1[word] == 1:
                if word not in s2:
                    s2[word] = 1
                else:
                    s2[word] += 1
        
        for word, freq in s2.items():
            if freq == 1:
                count += 1

        return count