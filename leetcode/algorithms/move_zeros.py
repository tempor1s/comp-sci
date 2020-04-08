class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0 # Pointer which skips zeros
        for _ in range(len(nums)):
            if nums[p] == 0:
                nums.pop(p)
                nums.append(0)
            else:
                p += 1
