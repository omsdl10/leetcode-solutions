class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        res="9"*100
        cur_cnt=0
        hm={}
        for i in range(n):
            if s[i]=='1':
                cur_cnt+=1
                hm[cur_cnt]=i
            if cur_cnt-k+1 in hm:
                prv_idx=hm[cur_cnt-k+1]
                if len(res)>(i-prv_idx+1):
                    res=s[prv_idx:i+1]
                elif len(res)==(i-prv_idx+1):
                    res=min(res,s[prv_idx:i+1])
        return res if res!="9"*100 else ""