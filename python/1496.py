# 1496. Path Crossing

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0)}
        pos = (0,0)

        for d in path:
            if d == "E":
                p = (1, 0)
            elif d == "W":
                p = (-1, 0)
            elif d == 'N':
                p = (0, 1)
            else:
                p = (0, -1)

            new_pos = (pos[0] + p[0], pos[1] + p[1])
            if new_pos in visited:
                return True
            else:
                visited.add(new_pos)
                pos = new_pos

        return False