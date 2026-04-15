class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def helper(i,j):
            q = deque([(i,j)])
            while q :
                y,x = q.popleft()
                for dirs in directions:
                    new_x = x + dirs[1]
                    new_y = y + dirs[0]
                    if (
                        new_x >= 0 and new_x < COLS and
                        new_y >= 0 and new_y < ROWS and
                        not visited[new_y][new_x] and
                        grid[new_y][new_x] == "1"):
                        q.append((new_y, new_x))
                        visited[new_y][new_x] = True
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and not visited[i][j]:
                    helper(i,j)
                    res += 1
        return res