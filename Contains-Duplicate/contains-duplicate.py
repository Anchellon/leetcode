class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # d = ()
        # for i in nums:
        #     if i not in d.keys():
        #         d.update({i:1})
        #     else:
        #         return True
        # return False
        
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return True
        return False
