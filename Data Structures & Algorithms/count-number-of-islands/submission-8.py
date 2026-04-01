class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        def helper(i,j):
            dq = deque([(i,j)])
            while dq:
                dy, dx = dq.popleft()
                for direction in directions:
                    new_y = dy + direction[0]
                    new_x = dx + direction[1]

                    if new_y >= 0 and new_y < ROWS and new_x >=0 and new_x < COLS and grid[new_y][new_x] == '1' and not visited[new_y][new_x]:
                        dq.append((new_y,new_x))
                        visited[new_y][new_x] = True

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and not visited[i][j]:
                    helper(i,j)
                    res += 1
        return res
                