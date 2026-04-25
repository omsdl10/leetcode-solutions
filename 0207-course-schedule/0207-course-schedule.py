class Solution:
    def canFinish(self, numCourses, prerequisites):
        matrix=[[0]*numCourses for _ in range(numCourses)]
        for a,b in prerequisites:
            matrix[b][a]=1
        state=[0]*numCourses
        def dfs(node):
            if state[node]==1:
                return False
            if state[node]==2:
                return True
            state[node]=1
            for neighbor in range(numCourses):
                if matrix[node][neighbor]==1:
                    if not dfs(neighbor):
                        return False
            state[node]=2
            return True
        for i in range(numCourses):
            if state[i]==0:
                if not dfs(i):
                    return False
        
        return True