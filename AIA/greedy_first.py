
import heapq

def greedy_best_first_search(graph, heuristic, start, goal):

    # Priority queue stores (heuristic value, current node)
    priority_queue = [(heuristic[start], start)]

    # To keep track of visited nodes
    visited = set()

    # To reconstruct the path
    parent = {start: None}

    while priority_queue:

        # Select node with the lowest heuristic value
        h, current = heapq.heappop(priority_queue)

        # Skip if already visited
        if current in visited:
            continue

        visited.add(current)

        # Check whether goal is reached
        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            return path[::-1]

        # Explore neighbouring nodes
        for neighbour in graph[current]:

            if neighbour not in visited:
                if neighbour not in parent:
                    parent[neighbour] = current

                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbour], neighbour)
                )

    return None


# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values (estimated distance to goal G)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

start = 'A'
goal = 'G'

path = greedy_best_first_search(graph, heuristic, start, goal)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("Goal not found")
