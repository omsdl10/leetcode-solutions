class Solution:
    def minimumPushes(self, word: str) -> int:
        counts=[word.count(chr(97+i)) for i in range(26)]
        counts=sorted(counts,reverse=True)
        res=0
        for idx,count in enumerate(counts):
            if(count==0):
                break
            res+=count*((idx//8)+1)
        return res



