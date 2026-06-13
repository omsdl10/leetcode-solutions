class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        visited=set()
        freq={}
        for i in range(len(s)):
            freq[s[i]]=i
        for i in range(len(s)):
            if s[i] in visited:
                continue
            while stack and stack[-1]>s[i] and i<freq[stack[-1]]:
                rem=stack.pop()
                visited.remove(rem)
            stack.append(s[i])
            visited.add(s[i])
        return "".join(stack)
            
