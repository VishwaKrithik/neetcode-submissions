class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = [0] * n

        def dfs(node):
            if visited[node]:
                return
            
            visited[node] = 1

            for nei in graph[node]:
                dfs(nei)

        
        connected = 0

        for node in range(n):
            if not visited[node]:
                dfs(node)
                connected += 1

        return connected