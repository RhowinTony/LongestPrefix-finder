class Solution:
    def longestcommonprefix(self, strs:list[str]) -> str:

        if len(strs) == 0:
            return ""
        
        minlen = len(strs[0])
        for i in range(len(strs)):
            minlen = min(len(strs[i]), minlen)
        
        