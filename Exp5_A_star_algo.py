import heapq
from collections import defaultdict

# Define a class for the graph node
class Node:
    def __init__(self, id, g, h):
        self.id = id
        self.g = g  # cost from start
        self.h = h  # heuristic estimate to goal

    # Comparator for priority queue (min-heap)
    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

# A* Search Algorithm
def astar(start, goal, graph, heuristic):
    pq = []  # Min-heap based on f = g + h
    heapq.heappush(pq, Node(start, 0, heuristic[start]))
    g_cost = defaultdict(lambda: float('inf'))  # Stores the cost to reach each node
    g_cost[start] = 0
    parent = {}  # Stores the path

    while pq:
        current = heapq.heappop(pq)
        if current.id == goal:  # Goal reached
            print("Path found: ", end="")
            node = goal
            path = []
            while node != start:
                path.append(str(node))
                node = parent[node]
            path.append(str(start))
            print(" -> ".join(reversed(path)))
            print(f"Total Cost: {g_cost[goal]}")
            return

        for neighbor, cost in graph[current.id]:
            new_g = g_cost[current.id] + cost
            if new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current.id
                heapq.heappush(pq, Node(neighbor, new_g, heuristic[neighbor]))

    print("No path found!")

def main():
    nodes = 10
    graph = defaultdict(list)

    # Example weighted graph (node, cost)
    graph[0] = [(1, 6), (5, 3)]
    graph[1] = [(2, 3), (3, 2)]
    graph[2] = [(3, 1), (4, 5)]
    graph[3] = [(4, 8)]
    graph[4] = [(8, 5), (9, 5)]
    graph[5] = [(6, 1), (7, 7)]
    graph[6] = [(8, 3)]
    graph[7] = [(8, 2)]
    graph[8] = [(9, 3)]

    # Heuristic values (estimated cost to reach goal)
    heuristic = [10, 8, 5, 7, 3, 6, 5, 3, 1, 0]

    start, goal = 0, 9
    print(f"A* Search from node {start} to node {goal}:")
    astar(start, goal, graph, heuristic)

if __name__ == "__main__":
    main()
