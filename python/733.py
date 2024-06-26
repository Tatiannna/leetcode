
# 733. Flood Fill


# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.


class Solution:
    
    def getNeighbors(self, pair, image, originalColor):
        row, col = pair
        neighbors = []

        dirs = [(0,1), (0, -1), (-1,0), (1,0)]

        for d in dirs:
            dx, dy = d
            newx = row + dx
            newy = col + dy

            if (newx < len(image) and newx >= 0 
                and newy < len(image[0]) and newy >= 0 and 
                image[newx][newy] == originalColor):

                neighbors.append((newx, newy))

        return neighbors

        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        queue = [(sr, sc)]
        originalColor = image[sr][sc]
        visited = set()


        while (len(queue) > 0):
            current = queue.pop(0)
            row, col = current
            visited.add(current)
            image[row][col] = color

            neighbors = self.getNeighbors(current, image, originalColor)

            for neighbor in neighbors:
                if neighbor not in visited:
                    nx, ny = neighbor
                    image[nx][ny] = color
                    queue.append(neighbor)
            
        return image