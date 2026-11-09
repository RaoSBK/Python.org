
# Hill Climbing Search Algorithm

def hill_climbing(graph, heuristic, start, goal):

    # Start from the initial node
    current = start

    # Store the path
    path = [current]

    while True:

        # If goal is reached, stop
        if current == goal:
            return path

        # Get neighbouring nodes
        neighbours = graph[current]

        # If no neighbours are available
        if not neighbours:
            return path

        # Select the neighbour with the lowest heuristic value
        next_node = min(neighbours, key=lambda node: heuristic[node])

        # If neighbour is not better, stop
        if heuristic[next_node] >= heuristic[current]:
            return path

        # Move to the better neighbour
        current = next_node
        path.append(current)


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

# Heuristic values (lower value means closer to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

# Initial and goal states
start = 'A'
goal = 'G'

# Call the function
result = hill_climbing(graph, heuristic, start, goal)

print("Path:", " -> ".join(result))

if result[-1] == goal:
    print("Goal reached!")
else:
    print("Local optimum reached. Goal not found.")
