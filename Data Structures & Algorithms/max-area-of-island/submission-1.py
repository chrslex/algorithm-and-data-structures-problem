class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = [[False for _ in range(m)] for _ in range(n)]
        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        res = 0

        def bfs(visited, i, j):
            q = deque([(i, j)])
            visited[i][j] = True
            count = 1
            while q :
                y, x = q.popleft()
                for dr in direction:
                    new_y = dr[0] + y
                    new_x = dr[1] + x

                    if(new_y in range(n) and
                        new_x in range(m) and
                        not visited[new_y][new_x] and
                        grid[new_y][new_x] == 1
                    ):
                        visited[new_y][new_x] = True
                        q.append((new_y, new_x))
                        count += 1
            return count
        
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 1 and not visited[i][j]):
                    c = bfs(visited, i, j)
                    res = max(c,res)
        return res