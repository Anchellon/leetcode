class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for i in s:
            if i not in ds:
                ds.update({i:s.count(i)})
        for i in t:
            if i not in dt:
                dt.update({i:t.count(i)})
        if(ds == dt):
            return True
        else:
            return False
