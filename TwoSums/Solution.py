class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            required_target = target - nums[i]
            if required_target in map:
                return [map[required_target],i]
            else:
                map[nums[i]]=i
            