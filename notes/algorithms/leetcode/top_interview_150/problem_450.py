from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if root is None:
        return root

    if root.val > key:
        root.left = delete_node(root.left, key)
        return root
    elif root.val < key:
        root.right = delete_node(root.right, key)
        return root
    else:
        # When root is equal to the target and there
        # is no left subtree.
        if root.left is None:
            return root.right
        # When root is equal to the target and there is
        # no right subtree.
        elif root.right is None:
            return root.left
        else:
            # When both left and right subtrees exists.

            # Find the smallest element in the right subtree.
            parent_node, chosen_node = root, root.right
            while chosen_node.left is not None:
                parent_node, chosen_node = chosen_node, chosen_node.left

            # The chosen_node is going to be either a leaf node
            # or a node with only the right subtree. If it indeed had a
            # left subtree tree, we would have chosen a node from that
            # as the chosen node in the above loop.
            if parent_node != root:
                parent_node.left = chosen_node.right
            else:
                parent_node.right = chosen_node.right

            # Update value of the root with the chosen node
            root.val = chosen_node.val

    return root


def in_order_traversal(node) -> None:
    if node is not None:

        queue = [node]

        while len(queue) > 0:
            this_node = queue.pop(0)

            if this_node is not None:
                print(this_node.val)
                if this_node.left is not None:
                    queue.append(this_node.left)
                else:
                    queue.append(None)
                if this_node.right is not None:
                    queue.append(this_node.right)
                else:
                    queue.append(None)
            else:
                print("null")


if __name__ == "__main__":
    node1 = TreeNode(4)
    node2 = TreeNode(7)
    node3 = TreeNode(6)
    node4 = TreeNode(5)
    node5 = TreeNode(8)
    node6 = TreeNode(9)

    node1.right = node2
    node2.left = node3
    node2.right = node5
    node3.left = node4
    node5.right = node6

    # in_order_traversal(node=node1)

    # single_node = TreeNode(0)
    res = delete_node(node1, key=4)
    in_order_traversal(res)
