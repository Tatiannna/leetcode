# 463. Island Perimeter

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. 
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


class Solution:

    def getStart(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return (i,j)
    
    def getNeighbors(self, point, grid):
        neighbors = []
        row, col = point
        dirs = [(0,1), (0, -1), (-1, 0), (1,0)]

        for d in dirs:
            dx, dy = d
            newx = dx + row
            newy = dy + col

            if (newx < len(grid) and newx >= 0 and newy >= 0 and newy < len(grid[0]) 
                and grid[newx][newy] == 1):
                neighbors.append((newx, newy))
        
        return neighbors

    def islandPerimeter(self, grid: List[List[int]]) -> int:
      
        perimeter = 0
        start = self.getStart(grid)
        visited = {start}
        queue = [start]

        while len(queue) > 0:
            current = queue.pop(0)
            neighbors = self.getNeighbors(current, grid)
            perimeter += 4 - len(neighbors)
            # print(f'{current} adds {4- len(neighbors)} to the total perimeter')
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return perimeter