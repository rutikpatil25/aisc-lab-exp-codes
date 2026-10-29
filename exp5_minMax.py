import math

class TreeNode:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def minimax_with_path(node, is_maximizing):
    if not node.children:
        return node.value, [node.name]

    if is_maximizing:
        max_eval = -math.inf
        best_path = []

        for child in node.children:
            eval_score, child_path = minimax_with_path(child, False)

            if eval_score > max_eval:
                max_eval = eval_score
                best_path = [node.name] + child_path

        return max_eval, best_path

    else:
        min_eval = math.inf
        best_path = []

        for child in node.children:
            eval_score, child_path = minimax_with_path(child, True)

            if eval_score < min_eval:
                min_eval = eval_score
                best_path = [node.name] + child_path

        return min_eval, best_path


if __name__ == "__main__":
    root = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')

    d = TreeNode('d', value=3)
    e = TreeNode('e', value=5)
    f = TreeNode('f', value=2)
    g = TreeNode('g', value=9)

    root.add_child(b)
    root.add_child(c)

    b.add_child(d)
    b.add_child(e)

    c.add_child(f)
    c.add_child(g)

    optimal_score, path_list = minimax_with_path(root, True)

    path_string = " -> ".join(path_list)

    print(f"Optimal Score: {optimal_score}")
    print(f"Optimal Path: {path_string}")