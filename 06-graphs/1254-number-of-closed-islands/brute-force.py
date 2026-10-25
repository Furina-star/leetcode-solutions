"""
Number of Closed Islands - Brute Force Approach
Algorithm: Repeated Depth-First Search
Time Complexity: O((m*n)^2)
Space Complexity: O(m*n)
"""

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def is_closed_island(start_row: int, start_col: int) -> bool:
            stack = [(start_row, start_col)]
            visited = {(start_row, start_col)}

            while stack:
                r, c = stack.pop()

                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    return False

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))

            return (start_row, start_col) == min(visited)

        closed_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if is_closed_island(r, c):
                        closed_islands += 1

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
