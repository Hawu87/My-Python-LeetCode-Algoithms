class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #max for array is the initial case
        #use binary search to arrive at a O(log(max(p)) * p)
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            if hours <= h:
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
        return res
