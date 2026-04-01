class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        res = 0

        def bfs(x, y, visited):
            directions = [[0,1], [1,0], [-1,0], [0,-1]]
            dq = deque([[x,y]])

            while(dq):
                xx,yy = dq.popleft()
                for direction in directions:
                    new_x = xx + direction[0]
                    new_y = yy + direction[1]

                    if new_x >= 0 and new_x < ROWS and new_y >= 0 and new_y < COLS and not visited[new_x][new_y] and grid[new_x][new_y] == "1":
                        dq.append([new_x, new_y])
                        visited[new_x][new_y] = True
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j, visited)
                    res += 1
        return res
                