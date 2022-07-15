class Solution:
    def longestcommonprefix(self, strs:list[str]) -> str:

        if len(strs) == 0:
            return ""
        
        minlen = len(strs[0])
        for i in range(len(strs)):
            minlen = min(len(strs[i]), minlen)
        
        lcp = ""
        i = 0
        while i < minlen:
            char = strs[0][i]
            for j in range(i,len(strs)):
                if strs[j][i] != char:
                    return lcp
            lcp = lcp + char
            i += 1

        return lcp