class Tree(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_sub_trees(tree):
    """Counts the sub-trees of the given tree.
    :param tree: The tree
    :return: The number of sub-trees
    """
    if not tree:  # Does not exist in the first place
        return 0

    # recursively find sub-trees on left and right subtrees and add the current node to the count.
    left = count_sub_trees(tree.left) + 1
    right = count_sub_trees(tree.right) + 1

    if left == 1 and right == 1:
        return 1                    # If the tree is a leaf
    elif left == 1:
        return right                # If there is only a right sub-tree
    elif right == 1:
        return left                 # If there is only a left sub-tree
    else:
        return left + right + 1     # subtrees with root+left, subtrees with root+right and the tree itself
