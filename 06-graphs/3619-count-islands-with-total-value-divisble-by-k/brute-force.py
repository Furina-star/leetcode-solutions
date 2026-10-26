"""
Count Islands with Total Value Divisible by K - Brute Force Approach
Algorithm: Repeated DFS
Time Complexity: O(m*n)^2
Space Complexity: O(m*n)
"""

from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        checked_islands = set()
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                stack = [(r, c)]
                visited = {(r, c)}
                total = 0

                while stack:
                    row, col = stack.pop()
                    total += grid[row][col]

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] > 0
                            and (nr, nc) not in visited
                        ):
                            visited.add((nr, nc))
                            stack.append((nr, nc))

                island_id = frozenset(visited)

                if island_id not in checked_islands:
                    checked_islands.add(island_id)

                    if total % k == 0:
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