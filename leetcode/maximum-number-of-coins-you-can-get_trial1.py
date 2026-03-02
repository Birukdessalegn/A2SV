class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        coins = 0
        for i in range(1, n, 2):
            if i >= n * 2 // 3:  # stop before Bob's part
                break
            coins += piles[i]
        return coins