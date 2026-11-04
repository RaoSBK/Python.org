import math

def minimax(depth, node_index, maximizing_player, values, max_depth):

    # Base case: Leaf node reached
    if depth == max_depth:
        return values[node_index]

    if maximizing_player:
        best = -math.inf

        for i in range(2):
            value = minimax(
                depth + 1,
                node_index * 2 + i,
                False,
                values,
                max_depth
            )
            best = max(best, value)

        return best

    else:
        best = math.inf

        for i in range(2):
            value = minimax(
                depth + 1,
                node_index * 2 + i,
                True,
                values,
                max_depth
            )
            best = min(best, value)

        return best


# Leaf nodes of the game tree
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Height of tree
max_depth = 3

result = minimax(
    depth=0,
    node_index=0,
    maximizing_player=True,
    values=values,
    max_depth=max_depth
)

print("Optimal Value:", result)