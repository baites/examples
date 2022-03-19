class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Transform the prerequisites into a directed graph
        # Create adjacent list
        adjacent = [[] for i in range(numCourses)]
        
        # Loop over prerequisites and make the graph edges
        for course, prereq in prerequisites:
            adjacent[prereq].append(course)
        
        # List of visited nodes
        visited = [False]*numCourses
        
        # Graph counter
        counter = 0
        
        # Postvisited counter
        postvisited = [0]*numCourses
        
        # Compute postvisited counter
        def postvisit(node):
            nonlocal counter
            counter += 1
            postvisited[node] = counter
                                
        # Recursive DFS
        def explore(node, node_counter=0):
            visited[node] = True
            for neighbor in adjacent[node]:
                if not visited[neighbor]:
                    explore(neighbor, node_counter)
            postvisit(node)
        
        # Start from all the different nodes and explore
        for node in range(numCourses):
            if not visited[node]:
                explore(node)
        
        # Check all the edges for violation of postvisited counter
        for node, neighbors in enumerate(adjacent):
            for neighbor in neighbors:
                if postvisited[node] <= postvisited[neighbor]:
                    return False
                
        return True
