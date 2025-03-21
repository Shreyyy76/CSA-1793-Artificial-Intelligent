class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children is not None else []

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Example usage:
if __name__ == "__main__":
    # Creating a simple game tree
    leaf_nodes = [Node(3), Node(5), Node(6), Node(9), Node(1), Node(2), Node(0), Node(-1)]
    intermediate_nodes = [Node(None, [leaf_nodes[0], leaf_nodes[1]]),
                          Node(None, [leaf_nodes[2], leaf_nodes[3]]),
                          Node(None, [leaf_nodes[4], leaf_nodes[5]]),
                          Node(None, [leaf_nodes[6], leaf_nodes[7]])]
    root = Node(None, [intermediate_nodes[0], intermediate_nodes[1], intermediate_nodes[2], intermediate_nodes[3]])

    # Running alpha-beta pruning on the game tree
    result = alpha_beta(root, 3, float('-inf'), float('inf'), True)
    print(f"Best value for the root is: {result}")
