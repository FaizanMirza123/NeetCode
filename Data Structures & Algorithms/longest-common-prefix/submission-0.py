class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res =""
        for i in range(len(strs[0])): 
            for s in strs: # dance ,dog
                if i == len(s) or s[i] != strs[0][i]: # first string ke letter se saray string ke first letter compare kro
                    return res
            res+=strs[0][i]
        return res