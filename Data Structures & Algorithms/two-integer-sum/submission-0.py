class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, v in enumerate(nums):
            compl = target - v

            if compl in hashMap:
                return [hashMap[compl], i]
            
            hashMap[v] = i