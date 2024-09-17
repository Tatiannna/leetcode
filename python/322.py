# 322. Coin Change
# https://leetcode.com/problems/coin-change/description/


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        queue = deque([(0,0)])
        computed = set()

        while queue:
            current, count = queue.popleft()

            if current == amount:
                return count

            for coin in coins:
                if current + coin <= amount and current + coin not in computed:
                    queue.append((current + coin, count + 1))
                    computed.add(current + coin)    

        return -1