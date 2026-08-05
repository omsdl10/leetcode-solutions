class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for u,v in invocations:
            graph[u].append(v)
        sus=set()
        q=deque([k])
        sus.add(k)
        while q:
            cur=q.popleft()
            for nei in graph[cur]:
                if nei not in sus:
                    sus.add(nei)
                    q.append(nei)       
        for u,v in invocations:
            if u not in sus and v in sus:
                return list(range(n))      
        return [i for i in range(n) if i not in sus]