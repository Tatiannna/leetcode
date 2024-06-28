
class Solution(object):
    
    def getNeighbors(self, point, grid, visited):
        neighbors = []
        row, col = point
        dirs = [(0,-1), (0, 1), (-1, 0), (1, 0)]
        for d in dirs:
            dx = row + d[0]
            dy = col + d[1]
            if (dx >= 0 and dx < len(grid) and dy >= 0 and dy < len(grid[0]) and grid[dx][dy] == 2147483647
                and (dx, dy) not in visited):
                visited.add((dx,dy))
                neighbors.append((dx,dy))
        return neighbors


    def wallsAndGates(self, grid):
        queue = []
        count = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row,col))
        while queue:
            length = len(queue)
            while length > 0:
                row, col = queue.pop(0)
                grid[row][col] = count
                neighbors = self.getNeighbors((row,col), grid, visited)
                for neighbor in neighbors:
                    queue.append(neighbor)
               length -=1
            count += 1
        return grid

        
        

        



