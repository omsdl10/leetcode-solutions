class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        storage=set()
        l=0
        result=0
        for i in range(len(s)):
            while s[i] in storage:
                storage.remove(s[l])
                l+=1
            storage.add(s[i])
            result=max(result,i-l+1)
        return result


