class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def greedy_coloring(self):
        # Sort vertices by degree in descending order
        vertices = sorted(range(self.V), key=lambda x: len(self.graph[x]), reverse=True)

        result = [-1] * self.V  # Initialize all vertices as unassigned
        result[vertices[0]] = 0  # Assign the first color to the first vertex

        # Assign colors to remaining vertices
        for u in vertices[1:]:
            available = [True] * self.V  # Mark all colors as available

            # Mark colors of adjacent vertices as unavailable
            for v in self.graph[u]:
                if result[v] != -1:
                    available[result[v]] = False

            # Find the first available color
            for color in range(self.V):
                if available[color]:
                    break

            result[u] = color

        for u in range(self.V):
            print(f"Vertex {u} --> Color {result[u]}")

        # Calculate the number of colors used
        num_colors_used = len(set(result))
        print(f"Number of colors used: {num_colors_used}")

# Example usage:
if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    print("Coloring of vertices:")
    graph.greedy_coloring()
