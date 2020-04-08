class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ht = dict()
        for n in nums:
            ht[n] = ht.get(n, 0) + 1
        return min(ht, key=ht.get)
        # res = 0
        # for num in nums:
        #     res ^= num
        # return res
