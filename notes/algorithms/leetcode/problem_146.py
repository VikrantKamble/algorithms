from typing import Optional


class DLNode:
    def __init__(
        self,
        key,
        value,
        parent: Optional["DLNode"] = None,
        next: Optional["DLNode"] = None,
    ):
        self.key = key
        self.value = value
        self.parent = parent
        self.next = next


class DLList:
    def __init__(self):
        self.head = None
        self.last_node = None

        self.count = 0

    def __len__(self) -> int:
        return self.count

    def insert(self, node: DLNode):
        if len(self) == 0:
            self.head = node
            self.last_node = node
        else:
            self.head.parent, node.next = node, self.head
            self.head = node
        self.count += 1

    def pop(self) -> Optional[DLNode]:
        """Remove the tail node."""
        node_to_be_returned = self.last_node

        if len(self) > 0:
            parent_node = self.last_node.parent

            if parent_node is not None:
                parent_node.next, self.last_node.parent = None, None
                self.last_node = parent_node
            else:
                self.last_node = None
                self.head = None

            self.count -= 1

        return node_to_be_returned

    def remove(self, node) -> DLNode:
        """Remove any given node."""
        parent_node, next_node = node.parent, node.next

        node.parent = None
        node.next = None

        if (next_node is None) and (parent_node is not None):
            parent_node.next = None
            self.last_node = parent_node
        elif (parent_node is None) and (next_node is not None):
            next_node.parent = None
            self.head = next_node
        elif (parent_node is not None) and (next_node is not None):
            parent_node.next, next_node.parent = next_node, parent_node
        else:
            self.head = None
            self.last_node = None

        self.count -= 1
        return node

    def remove_and_insert(self, node) -> None:
        self.insert(self.remove(node))


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.lru_ds = DLList()

    def get(self, key: int) -> int:
        node = self.hash_map.get(key, None)

        # In case the key doesn't exists, simply return -1
        if node is None:
            return -1
        else:
            # Logic to update the underlying LRU DS
            self.lru_ds.remove_and_insert(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            # If key already exists, we update its value
            print("Key already exists, updating its value")
            this_node = self.hash_map[key]

            # update the value of the node
            this_node.value = value

            # Also since we touched this node, we need to put
            # it at the front
            self.lru_ds.remove_and_insert(this_node)

        else:
            # Check for overflow
            if len(self.hash_map) == self.capacity:
                lru_node = self.lru_ds.pop()
                self.hash_map.pop(lru_node.key)

            # Insert a new key into the hash_map
            node = DLNode(key=key, value=value)
            self.hash_map[key] = node

            # Also insert the node into the LRU DS at the head
            # since its the most recent.
            self.lru_ds.insert(node)


if __name__ == "__main__":
    obj = LRUCache(2)
    print(obj.put(2, 1))
    print(obj.put(1, 1))
    print(obj.put(2, 3))
    print(obj.put(4, 1))
    print(obj.get(1))
    print(obj.get(2))
