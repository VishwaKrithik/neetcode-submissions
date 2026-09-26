class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        

        def topo_sort():
            q = deque()
            res = 0

            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)
                    res += 1

            
            while q:
                node = q.popleft()

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
                        res += 1
            
            print(res)
            return res == numCourses
    

        return topo_sort()