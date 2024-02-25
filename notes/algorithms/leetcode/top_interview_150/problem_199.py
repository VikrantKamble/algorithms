from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    solution = []

    # Super base case
    if root is None:
        return solution

    # We will use two queues for this. All the children of each
    # node in a given stack will be dumped into other stack
    # and vice-versa
    queue_1 = []
    queue_2 = [root]

    while True:
        # We always use queue_1 as the main queue to pop from
        while len(queue_1) > 0:
            node = queue_1.pop(0)

            # Put the children in the other queue
            if node.left is not None:
                queue_2.append(node.left)
            if node.right is not None:
                queue_2.append(node.right)

        if len(queue_1) == 0:
            if len(queue_2) == 0:
                break
            else:
                # The topmost element is the rightmost element for this level.
                solution.append(queue_2[-1].val)
                queue_1, queue_2 = queue_2, queue_1

    return solution


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(5)
    node5 = TreeNode(4)

    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.right = node5

    print(right_side_view(node1))
