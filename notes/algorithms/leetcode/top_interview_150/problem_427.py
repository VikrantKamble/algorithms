from typing import List


class Node:
    def __init__(
        self,
        val,
        isLeaf,
        topLeft,
        topRight,
        bottomLeft,
        bottomRight,
    ) -> None:
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class ZoomNode:
    def __init__(self, width, x_pos, y_pos):
        self.width = width
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.is_leaf = False
        self.val = 1

        self.topLeft = None
        self.topRight = None
        self.bottomLeft = None
        self.bottomRight = None


def construct(grid: List[List[int]]) -> Node:
    def construct_zoom_node(width, x_pos, y_pos) -> ZoomNode:

        this_node = ZoomNode(width, x_pos, y_pos)

        # base case: leaf node spanning a single element
        if width > 1:

            # Else add the children
            new_width = width // 2

            top_left_node = construct_zoom_node(
                width=new_width, x_pos=x_pos, y_pos=y_pos
            )

            top_right_node = construct_zoom_node(
                width=new_width, x_pos=x_pos, y_pos=y_pos + new_width
            )
            bottom_left_node = construct_zoom_node(
                width=new_width, x_pos=x_pos + new_width, y_pos=y_pos
            )
            bottom_right_node = construct_zoom_node(
                width=new_width, x_pos=x_pos + new_width, y_pos=y_pos + new_width
            )

            # Check if we can coalese the subgrids into one
            check_val = top_left_node.val

            if (
                top_left_node.is_leaf
                and top_right_node.is_leaf
                and bottom_left_node.is_leaf
                and bottom_right_node.is_leaf
                and (top_right_node.val == check_val)
                and (bottom_left_node.val == check_val)
                and (bottom_right_node.val == check_val)
            ):
                this_node.val = check_val
                this_node.is_leaf = True
            else:
                this_node.topLeft = top_left_node
                this_node.topRight = top_right_node
                this_node.bottomLeft = bottom_left_node
                this_node.bottomRight = bottom_right_node
        else:
            this_node.val = grid[x_pos][y_pos]
            this_node.is_leaf = True

        return this_node

    root_zoom_node = construct_zoom_node(len(grid), x_pos=0, y_pos=0)

    # Now we need to create the same tree but with using Node
    # instead of ZoomNode
    def reconstruct(zoom_node: ZoomNode) -> Node:
        node = Node(zoom_node.val, int(zoom_node.is_leaf), None, None, None, None)

        if not zoom_node.is_leaf:
            node.topLeft = reconstruct(zoom_node.topLeft)
            node.topRight = reconstruct(zoom_node.topRight)
            node.bottomLeft = reconstruct(zoom_node.bottomLeft)
            node.bottomRight = reconstruct(zoom_node.bottomRight)

        return node

    return reconstruct(zoom_node=root_zoom_node)


def in_order_traversal(node: Node) -> None:
    queue = [node]

    while len(queue) > 0:
        this_node = queue.pop(0)

        if this_node is not None:
            print([this_node.isLeaf, this_node.val])
        else:
            print("null")

        # Push children into the queue
        if this_node is not None:
            if not this_node.isLeaf:
                queue.append(this_node.topLeft)
                queue.append(this_node.topRight)
                queue.append(this_node.bottomLeft)
                queue.append(this_node.bottomRight)


if __name__ == "__main__":
    node = construct(
        grid=[
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
        ]
    )
    in_order_traversal(node)
