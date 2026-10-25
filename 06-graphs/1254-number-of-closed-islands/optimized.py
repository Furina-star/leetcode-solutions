"""
Number of Closed Islands - Optimized Approach
Algorithm: Depth-First Search / Bread-First Search
Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if rows < 3 or cols < 3:
            return 0

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def flood_fill(start_row: int, start_col: int) -> None:
            stack = [(start_row, start_col)]
            grid[start_row][start_col] = 1

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        stack.append((nr, nc))

        for c in range(cols):
            if grid[0][c] == 0:
                flood_fill(0, c)
            if grid[rows - 1][c] == 0:
                flood_fill(rows - 1, c)

        for r in range(rows):
            if grid[r][0] == 0:
                flood_fill(r, 0)
            if grid[r][cols - 1] == 0:
                flood_fill(r, cols - 1)

        closed_islands = 0

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands += 1
                    flood_fill(r, c)

        return closed_islands

def main():
    grid = [
        [1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]
        ]

    solution = Solution()
    result = solution.closedIsland(grid)

    print(result)

if __name__ == "__main__":
    main()