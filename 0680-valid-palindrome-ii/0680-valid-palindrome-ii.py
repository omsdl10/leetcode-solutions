class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                drop_left=s[l+1:r+1]
                drop_right=s[l:r]
                
                return drop_left==drop_left[::-1] or drop_right==drop_right[::-1]
                
        return True