import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sorted_list(head: Optional[ListNode]) -> Optional[ListNode]:
    sorted_list = []

    while head is not None:
        heapq.heappush(sorted_list, -1 * head.val)
        head = head.next

    # Rebuild the list
    new_head = None
    while len(sorted_list) > 0:
        this_node = ListNode(-1 * heapq.heappop(sorted_list))
        if new_head is None:
            new_head = this_node
        else:
            this_node.next, new_head = new_head, this_node

    return new_head


if __name__ == "__main__":
    nums = [-1, 5, 3, 4, 0]

    new_head = None
    for val in nums:
        this_node = ListNode(val)
        if new_head is None:
            new_head = this_node
        else:
            this_node.next, new_head = new_head, this_node

    res = sorted_list(new_head)
    while res is not None:
        print(res.val)
        res = res.next
