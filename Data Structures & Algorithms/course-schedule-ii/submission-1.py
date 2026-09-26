from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        
        def topo_sort():
            res = []

            q = deque()

            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)
                

            while q:
                node = q.popleft()

                res.append(node)

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            
            print(res)
            return res
        
        res = topo_sort()
        return res if len(res) == numCourses else []
