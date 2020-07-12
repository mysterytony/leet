class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        min_so_far = prices[0]
        max_so_far = 0
        it = iter(prices)
        next(it)
        for n in it:
            if n - min_so_far > max_so_far:
                max_so_far = n - min_so_far
            if n < min_so_far:
                min_so_far = n
        return max_so_far
