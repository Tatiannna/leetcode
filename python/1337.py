class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = {}
        # keys 

        

        for i in range(len(mat)):
            current = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    current += 1
                else:
                    break
            if current not in counts:
                counts[current] = [i]
            else:
                counts[current].append(i)

        solution = []
        i = 0
        while len(solution) < k:
            if i in counts:
                for val in counts[i]:
                    solution.append(val)
                    if len(solution) == k:
                        break
            i += 1