# 3274. Check if Two Chessboard Squares Have the Same Color

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        rows = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

        return (abs(rows[coordinate1[0]] - rows[coordinate2[0]]) + abs(int(coordinate1[1]) - int(coordinate2[1]))) % 2 == 0