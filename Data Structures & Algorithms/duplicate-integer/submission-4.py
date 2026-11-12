class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_ds = set()
        for i in range(len(nums)):
            if nums[i] in hash_ds:
                return True
            else:
                hash_ds.add(nums[i])
        return False