class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # ht = {}
        # for item in nums:
        #     if item in ht:
        #         return True
        #     ht[item] = 1
        # return False
        return len(set(nums)) < len(nums)
