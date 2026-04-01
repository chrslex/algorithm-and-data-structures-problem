class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        d = {}

        for i in range(n):
            target = ''.join(sorted(strs[i]))
            if(target in d):
                d[target].append(strs[i])
            else:
                d[target] = [strs[i]]
        
        res = []
        for v in d.values():
            res.append(v)
        
        return res