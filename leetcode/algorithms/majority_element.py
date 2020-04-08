from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for item in nums:
            counter[item] = counter.get(item, 0) + 1

        return max(counter, key=counter.get)
        # return Counter(nums).most_common(1)[0][0]
