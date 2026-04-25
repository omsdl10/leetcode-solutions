class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[0]*numCourses for i in range(numCourses)]
        for a,b in prerequisites:
            graph[b][a]=1
        start=[0]*numCourses
        order=[]
        def dfs(node):
            if start[node]==1:
                return False
            if start[node]==2:
                return True
            start[node]=1
            for i in range(numCourses):
                if graph[node][i]==1:
                    if not dfs(i):
                        return False
            start[node]=2
            order.append(node)
            return True
        for i in range(numCourses):
            if start[i]==0:
                if not dfs(i):
                    return []

        return order[::-1]