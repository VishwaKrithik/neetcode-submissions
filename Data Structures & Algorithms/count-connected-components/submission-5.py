class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        visited = [False] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if not visited[node]:
                visited[node] = True
                for nei in graph[node]:
                    dfs(nei)


        count = 0
        for node in range(n):
            if not visited[node]:
                count += 1
                dfs(node)
    
        return count
