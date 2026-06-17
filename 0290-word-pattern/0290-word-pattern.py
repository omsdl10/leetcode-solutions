class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hmap={}
        new=s.split()
        newset1=set(new)
        newset2=set()
        for i in pattern:
            newset2.add(i)
        if len(newset1)!=len(newset2):
            return False
        if len(new)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in hmap:
                if hmap[pattern[i]]!=new[i]:
                    return False
            else:
                hmap[pattern[i]]=new[i]
        return True
                