class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        def bfs(i,j, visited):
            dequ = deque([(i,j)])
            visited[i][j] = 1
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            while dequ:
                y,x = dequ.popleft()
                for direction in directions:
                    new_x = x + direction[1]
                    new_y = y + direction[0]

                    if new_x < COLS and new_x >=0 and new_y < ROWS and new_y >= 0 and visited[new_y][new_x] != 1 and grid[new_y][new_x] == "1":
                        dequ.append((new_y, new_x))
                        visited[new_y][new_x] = 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and visited[i][j] != 1:
                    bfs(i, j, visited)
                    res += 1
        return res
            