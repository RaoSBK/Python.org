# Alpha-Beta Pruning Algorithm

MAX = 1000
MIN = -1000

def minimax(depth, node_index, maximizing_player, values, alpha, beta):

    # Base condition: If leaf node is reached
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        best = MIN

        # Check the left and right child nodes
        for i in range(2):
            val = minimax(
                depth + 1,
                node_index * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning condition
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        # Check the left and right child nodes
        for i in range(2):
            val = minimax(
                depth + 1,
                node_index * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta Pruning condition
            if beta <= alpha:
                break

        return best


# Main program
if __name__ == "__main__":

    # Leaf node values
    values = [3, 5, 6, 9, 1, 2, 0, -1]

    # Call the minimax function
    result = minimax(0, 0, True, values, MIN, MAX)

    print("The optimal value is:", result)