class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        pairs = []

        for num1 in arr:
            for num2 in arr:
                if (num1 + num2) % k == 0:
                    s = {num1, num2}
                    if s not in pairs:
                        pairs.append(s)
        return len(pairs) == len(arr)/2