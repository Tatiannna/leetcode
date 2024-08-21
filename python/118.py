118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        if numRows > 1:
            res.append([1,1])


        for i in range(3, numRows+ 1): 
            row = [1]

            i = 0
            while i < len(res[len(res) - 1]) - 1:
                print(res)
                row.append( res[len(res) - 1][i]   +     res[len(res) - 1][i + 1] )
                i += 1

            row.append(1)
            res.append(row)
            row = []

        return res