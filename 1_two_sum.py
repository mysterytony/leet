class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {} # num -> index
        for i, n in enumerate(nums):
            if (target - n) in num_set:
                return [i, num_set[target - n]]
            num_set[n] = i
        return []
