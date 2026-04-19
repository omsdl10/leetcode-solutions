class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hmap={}
        start=0
        end=0
        result=0
        while end<len(fruits):
            hmap[fruits[end]]=hmap.get(fruits[end], 0) + 1
            while len(hmap)>2:
                hmap[fruits[start]]-=1
                if hmap[fruits[start]]==0:
                    del hmap[fruits[start]]
                start+=1
            
            result=max(result,end-start+1)
            end+=1
        return result
            
                