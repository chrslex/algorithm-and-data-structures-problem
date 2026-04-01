class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        COLS = len(grid[0])
        ROWS = len(grid)
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(i, j, visited):
            q = deque([(i,j)])
            visited[i][j] = True

            while q:
                y,x = q.popleft()
                for direction in directions:
                    new_y = y + direction[0]
                    new_x = x + direction[1]

                    if new_y < ROWS and new_y >= 0 and new_x >=0 and new_x < COLS and not visited[new_y][new_x] and grid[new_y][new_x] == "1":
                        visited[new_y][new_x] = True
                        q.append((new_y, new_x))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i,j, visited)
                    res += 1
        
        return res