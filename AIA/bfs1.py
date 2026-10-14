graph = {
    "A" : ['B', 'C'],
    "B" : ['D', 'E'],
    'C' : ['F'],
    'D' : ['F'],
    'E' : [],
    'F' : []
}


visited = []



def dfs(node, visited, graph):
    if node not in visited:
        visited.append(node)
        print(node, end="")

        for neighbour in graph[node]:
            dfs(neighbour, visited, graph)



dfs('A', visited, graph)

