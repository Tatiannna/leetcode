
# 200. Number of Islands


# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting 
# adjacent lands horizontally or vertically. You may assume all four
#  edges of the grid are all surrounded by water.

# todo

class Solution:

    # get count of all lands
    # add to queue, BFS to get all neighbors
    # if visited is less than the count of all lands, then there is another island
    # increase island count by 1
    # if visited count is less than total land count, add an UNVISITED to queue, and BFS
    # increase island count by 1 
    # repeat until counts are equal

    def getNeighbors(self, grid, start):
        row, col = start
        dirs = [(-1,0), (1,0), (0,1), (0, -1)]
        neighbors = []

        for d in dirs:
            dx, dy = d[0] + row, d[1] + col

            if ( dx >= 0 and dx < len(grid) and dy >= 0 and dy < len(grid[0]) 
                and grid[dx][dy] == '1'):
                neighbors.append((dx,dy))

        return neighbors

        
    def numIslands(self, grid: List[List[str]]) -> int:

        land = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    land.append((i,j))

        count = 1 if land else 0

        queue = [land[0]]
        #visited = set(land[0])
        visited = set()

        while queue:
            current = queue.pop(0)
            visited.add(current)

            if current in land: # revisit, condition should always be met
                land.remove(current)
            neighbors = self.getNeighbors(grid, current)

            if neighbors:
                for n in neighbors:
                    queue.append(n)
                    visited.add(n)
            
            if len(land) > 0:
                count += 1
                queue.append(land[0])

        return count