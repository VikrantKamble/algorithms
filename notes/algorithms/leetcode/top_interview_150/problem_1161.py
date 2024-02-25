from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_level_sum(root) -> int:

    # Stack_1 will be used to compute the level sum
    stack_1 = [root]

    # Stack 2 will be used to store the children of all the nodes
    # of a given level and then swapped with stack_1
    stack_2 = []

    max_sum = float("-inf")
    k, maximal_level = 1, 1

    while True:
        curr_sum = 0
        while len(stack_1) > 0:
            node = stack_1.pop()

            # Compute the sum of this level.
            curr_sum += node.val

            # Add the children of this node to the
            # other stack to continue the loop.
            if node.left is not None:
                stack_2.append(node.left)
            if node.right is not None:
                stack_2.append(node.right)

        # If the sum is larger than the global max, set
        # the maximal level to this level.
        if curr_sum > max_sum:
            max_sum, maximal_level = curr_sum, k

        if len(stack_1) == 0:
            if len(stack_2) == 0:
                # If both stacks are empty, it implies all the
                # levels have been traversed.
                break
            stack_1, stack_2 = stack_2, stack_1
            k += 1

    return maximal_level


if __name__ == "__main__":
    node1 = TreeNode(-100)
    node2 = TreeNode(7)
    node3 = TreeNode(0)
    node4 = TreeNode(7)
    node5 = TreeNode(-8)

    # node1.left = node2
    # node1.right = node3
    # node2.left = node4
    # node2.right = node5

    print(max_level_sum(node1))
