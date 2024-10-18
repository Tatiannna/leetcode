# 3222. Find the Winning Player in Coin Game


class Solution:
    def losingPlayer(self, x: int, y: int) -> str:

        turns_played = 0

        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            turns_played += 1
            
        return 'Alice' if turns_played % 2 == 1 else 'Bob'