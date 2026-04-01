class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        
        
        def bfs(grid, visited, i, j) :
            dequ = deque([(i,j)])
            visited[i][j] = 1
            direction = [[0,1], [1,0], [-1,0], [0,-1]]
            
            while dequ :
                y,x = dequ.popleft()
                for d in direction:
                    new_x = x + d[1]
                    new_y = y + d[0]

                    if(
                        new_x in range(m) and
                        new_y in range(n) and
                        visited[new_y][new_x] != 1 and
                        grid[new_y][new_x] == '1'
                    ):
                        visited[new_y][new_x] = 1
                        dequ.append((new_y, new_x))
        
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == '1' and visited[i][j] != 1):
                    bfs(grid, visited, i , j)
                    res += 1
        return res