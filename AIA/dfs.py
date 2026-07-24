graph ={
    'A':['B','C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['H'],
    'F': [],
    'H': []
}


visited = []

def dfs(visited, graph, node):
    #check if the node is visited or not
    if node not in visited:
        visited.append(node)
        print(node, end="")

        #visited all neighbour recursion

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')