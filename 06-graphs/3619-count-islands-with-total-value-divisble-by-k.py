"""
Count Islands with Total Value Divisible by K
Algorithm:Iterative Depth-First Search / Bread-First Search
Time Complexity: O(m*n)
Space Complexity: O(m*n)
"""

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def flood_fill(start_row: int, start_col: int) -> int:
            total = grid[start_row][start_col]
            grid[start_row][start_col] = 0
            stack = [(start_row, start_col)]

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                        total += grid[nr][nc]
                        grid[nr][nc] = 0
                        stack.append((nr, nc))

            return total

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    island_total = flood_fill(r, c)
                    if island_total % k == 0:
                        count += 1

        return count

def main():
    grid = [
        [0, 2, 1, 0, 0],
        [0, 5, 0, 0, 5],
        [0, 0, 1, 0, 0],
        [0, 1, 4, 7, 0],
        [0, 2, 0, 0, 8]
    ]

    k = 5

    solution = Solution()
    result = solution.countIslands(grid, k)

    print(result)

if __name__ == "__main__":
    main()
