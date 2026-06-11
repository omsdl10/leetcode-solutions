class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mp ={chr(ord('A')+i):i+1 for i in range(26)}
        n=0
        summ=0
        for i in range(len(columnTitle)-1,-1,-1):
            summ=summ+((26**n)*mp[columnTitle[i]])
            n+=1
        return summ
