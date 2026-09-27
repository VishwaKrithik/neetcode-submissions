class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in p:
            graph[v].append(u)
            indegree[u] += 1
        

        q = deque()

        for node in range(n):
            if not indegree[node]:
                q.append(node)

        order = []
        
        while q:
            node = q.popleft()
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
    
        return order if len(order) == n else []