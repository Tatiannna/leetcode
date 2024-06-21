# 463. Island Perimeter

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. 
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# todo

class Solution:

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

        ''' If a block IS land it adds to the perimeter in proportion
            to the amount of neightbor blocks that are NOT land

            1. choose block, maybe with plain nested for loop, if not land, go to adjacent until land is found
            2. At each land
                0. Add land to visited
                1 Get neighbors and Count how many adjacent are NOT land and add this to perimeter
                2. Keep track of visited, do not double visit
                3. Go to next adjacent if there is an unvisited adjacent

        '''        
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)

        queue = [start]
        visited = set()

        while len(queue) > 0:
            current = queue.pop(0)
            visited.add(current)
            neighbors = self.getNeighbors(current, grid)
            perimeter += 4 - len(neighbors)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

        return perimeter