from collections import defaultdict 

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if not visited.get(i, False):  
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = {key: False for key in self.graph}  
        for node in self.graph:
            visited[node] = False 
        
        self.DFSUtil(v, visited)

    def DFSAll(self):  
        visited = {key: False for key in self.graph}
        for node in self.graph:
            if not visited[node]:
                self.DFSUtil(node, visited)
                print()
g = Graph()   
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print ("Following is DFS from (starting from vertex 2)") 
g.DFS(2)
