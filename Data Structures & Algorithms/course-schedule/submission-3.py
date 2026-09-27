class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for u, v in p:
            graph[v].append(u)
        
        state = [0] * n

        def dfs(node):
            state[node] = 1

            for nei in graph[node]:
                if state[nei] == 1:
                    return True
                if state[nei] == 0:
                    if dfs(nei):
                        return True
            
            state[node] = 2
            return False
        

        for node in range(n):
            if state[node] == 0:
                if dfs(node):
                    return False

        return True
