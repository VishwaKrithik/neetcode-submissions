class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)



        def dfs(node):
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        
        connected = 0

        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                connected += 1

        return connected