class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for anagram in strs:
            sorted_anagram = "".join(sorted(anagram))
            if sorted_anagram not in d:
                d[sorted_anagram] = [anagram]
            else:
                d[sorted_anagram].append(anagram)
        
        return [values for key,values in d.items()]
        