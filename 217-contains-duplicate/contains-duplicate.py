class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       separate_set=set(nums)
       if len(separate_set)<len(nums):
            return True
       else:
            return False
        