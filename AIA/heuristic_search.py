
# Heuristic Search (Greedy Best-First Search)

def heuristic_search(graph, heuristic, start, goal):

    # Store the starting node
    open_list = [start]

    # Track visited nodes
    visited = set()

    # Store the path
    parent = {start: None}

    while open_list:

        # Select the node having the lowest heuristic value
        current = min(open_list, key=lambda node: heuristic[node])

        open_list.remove(current)

        # Skip already visited nodes
        if current in visited:
            continue

        visited.add(current)

        # Check whether the goal is reached
        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            return path[::-1]

        # Visit neighbouring nodes
        for neighbour in graph[current]:

            if neighbour not in visited and neighbour not in parent:
                parent[neighbour] = current
                open_list.append(neighbour)

    return None


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

# Starting and goal nodes
start = 'A'
goal = 'G'

# Run the algorithm
result = heuristic_search(graph, heuristic, start, goal)

if result:
    print("Path:", " -> ".join(result))
else:
    print("Goal not found")
