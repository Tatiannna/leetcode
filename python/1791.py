# 1791. Find Center of Star Graph


# There is an undirected star graph consisting of n nodes labeled from 1 to n. 
# A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
#  that there is an edge between the nodes ui and vi. Return the center of the given star graph.

#todo

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph = {}
        nums = set()

        for edge in edges:
            for node in edge:
                graph[node[0]] = node[1]
                graph[node[1]] = node[2]
                set.add(node[0])
                set.add(node[1])
            
        
        count = 0
        for num in set:
            if graph[num]:
                count += 1
            if count >= 2* len(graph):
                return True

        return False