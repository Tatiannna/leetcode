
# 200. Number of Islands


# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting 
# adjacent lands horizontally or vertically. You may assume all four
#  edges of the grid are all surrounded by water.

# todo
class Solution:

    def get_neighbors(self, grid, point):
        x, y = point
        dirs = [(1,0), (-1, 0), (0,1), (0, -1)]
        neighbors = []

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if ( 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1'):
                neighbors.append((nx, ny))
        return neighbors
            
    def numIslands(self, grid: List[List[str]]) -> int:

        ans = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    queue = [(i,j)]

                    while queue:
                        current = queue.pop()
                        visited.add(current)

                        neighbors = self.get_neighbors(grid, current)

                        for neighbor in neighbors:
                            if neighbor not in visited:
                                queue.append(neighbor)
                                visited.add(neighbor)
                    ans += 1
        
        return ans