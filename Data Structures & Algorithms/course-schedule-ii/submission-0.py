class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        

        def topo_sort():
            q = deque()
            res = []

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


            return res


        res = topo_sort()
        return [] if len(res) != numCourses else res