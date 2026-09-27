class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in p:
            graph[v].append(u)
            indegree[u] += 1
        

        q = deque()

        for node in range(n):
            if not indegree[node]:
                q.append(node)

        count = 0    
        
        while q:
            node = q.popleft()
            count += 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
    
        return count == n
                