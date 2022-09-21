ass Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        ans = []
        for i in range (0, len(nums)):
            if nums[i] not in d:
                d.update({nums[i]:[i]})
            else:
                d[nums[i]].append(i)
        for i in range (0, len(nums)):
            if target - nums[i] != nums[i] and target - nums[i] in d:
                return [d[target - nums[i]][0],d[nums[i]][0]]
            elif target - nums[i] == nums[i] and len(d[nums[i]]) > 1:
                return [d[nums[i]][0],d[nums[i]][1]]
        return ans
