class Node:
    key: int
    value: int
    freq_counter: int

    def __init__(self, key: int, value: int) -> None:
        self.freq_counter = 1
        self.key = key
        self.value = value
        self.next = self.prev = None


class FreqLinkedList:
    head: Node
    recency_table: dict[int, Node]  # key: freq_counter

    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.recency_table = {}

    def update_node(self, node: Node):
        freq_counter = node.freq_counter
        # Remove node from linked list
        prev_node = node.prev
        if node.next != None:
            node.next.prev = prev_node
        prev_node.next = node.next
        # If node itself is most recency of freq_counter, update value of freq_counter in recency table
        if self.recency_table[freq_counter] == node:
            if prev_node.freq_counter != freq_counter:
                del self.recency_table[freq_counter]
            else:
                self.recency_table[freq_counter] = prev_node

        # Update node itself
        node.freq_counter = freq_counter + 1
        # Append
        # Determine which key in recency table, node will be append
        key_to_append = prev_node.freq_counter
        if self.recency_table.get(freq_counter) is not None:
            key_to_append = freq_counter
        if self.recency_table.get(freq_counter + 1) is not None:
            key_to_append = freq_counter + 1

        node_to_append = self.recency_table[key_to_append]
        node.next = node_to_append.next
        if node_to_append.next is not None:
            node_to_append.next.prev = node
        node_to_append.next = node
        node.prev = node_to_append

        # Node now is most recency of freq_counter + 1 in recency table
        self.recency_table[freq_counter + 1] = node

    def pop_least_freq_node(self) -> Node:
        lrn = self.head.next
        self.head.next = lrn.next
        if lrn.next is not None:
            lrn.next.prev = self.head
        if self.recency_table.get(lrn.freq_counter) == lrn:
            del self.recency_table[lrn.freq_counter]
        return lrn

    def append(self, node: Node):
        if node.freq_counter != 1:
            raise ValueError("Freq of new node for append operation must be 1")
        node_to_append = self.head
        if self.recency_table.get(1) is not None:
            node_to_append = self.recency_table[1]

        node.next = node_to_append.next
        if node_to_append.next is not None:
            node_to_append.next.prev = node
        node_to_append.next = node
        node.prev = node_to_append

        self.recency_table[1] = node

    def show(self):
        cur_p = self.head.next
        r = []
        while (cur_p is not None):
            r.append(f"({cur_p.key},{cur_p.value},{cur_p.freq_counter})")
            cur_p = cur_p.next
        print('->'.join(r))
        print('recency_table', self.recency_table.keys())


class LFUCache:
    capacity: int
    value_table: dict[int, Node]  # key: key
    freq_linked_list: FreqLinkedList

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.value_table = {}
        self.freq_linked_list = FreqLinkedList()

    def get(self, key: int) -> int:
        if self.value_table.get(key) is None:
            return -1
        n = self.value_table[key]
        # Update freq_linked_list
        self.freq_linked_list.update_node(n)
        return n.value

    def put(self, key: int, value: int) -> None:
        if self.value_table.get(key) is not None:
            # Capacity is still the same after this operation, but freq_linked_list need to update internally
            n = self.value_table[key]
            n.value = value
            # Update freq_linked_list
            self.freq_linked_list.update_node(n)
        else:
            # Not enough capacity
            if len(self.value_table) == self.capacity:
                # Pop the least freq node
                lfn = self.freq_linked_list.pop_least_freq_node()
                del self.value_table[lfn.key]
            new_node = Node(key, value)
            self.freq_linked_list.append(new_node)
            self.value_table[key] = new_node

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def exec(inputs, operations):
    capacity = inputs[0][0]
    lfu_cache = LFUCache(capacity)
    for i in range(1, len(operations)):
        op = operations[i]
        inp = inputs[i]
        if op == "get":
            v = lfu_cache.get(inp[0])
            # print(v)
        else:
            key, value = inp
            lfu_cache.put(key, value)
            # print('null')
        print('* i', i, ', op', op, ', inp', inp)
        print('value_table', lfu_cache.value_table.keys())
        lfu_cache.freq_linked_list.show()


# Example Case
operations = ["LFUCache", "put", "put", "get",
              "put", "get", "get", "put", "get", "get", "get"]
inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

# capacity = 2
# value_table = {
#   4: Node(4, 4, 2)
#   3: Node(3, 3, 3)
# }
# freq_linked_list: Head = Node(-1 -1, 1) <-> Node(4, 4, 2) <-> Node(3, 3, 3) -> NULL
# recency_table = {
#   1: Node(-1, -1, 1)
#   2: Node(4, 4, 2)
#   3: Node(3, 3, 3)
# }
# node = Node(4, 4, 2)
# key_to_append = 1
# node_to_append = Node(-1, -1, 1)

# i = 10, get(4)
# null, null, null, 1, null, -1, 3, null, -1, 3, 4

# exec(inputs, operations)


# Corner case
# capacity = 1
operations = ["LFUCache", "put", "put", "get", "get"]
inputs = [[1], [1, 1], [2, 2], [1], [2]]

# capacity = 1
# value_table = {
#   2: Node(2, 2, 2)
# }
# freq_linked_list: Head = Node(-1 -1, 1) -> Node(2, 2, 2)
# recency_table = {
#   2: Node(2, 2, 2)
# }
# null, null, null, -1, 2

# exec(inputs, operations)


# has same freq until exceed capacity
operations = ["LFUCache", "put", "put", "put", "put", "put", "get"]
inputs = [[4], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1]]
# Expected = [...null, -1]

# exec(inputs, operations)


# recency_table = { 1: Node(1, 1) -> 2: Node(2, 2) -> 3: Node(3, 3)},  put (2, 3)
# Expected: recency_table = {1: Node(1, 1) -> 3: Node(3, 3) -> Node(2, 3)}
operations = ["LFUCache", "put", "put", "get", "put", "put", "get", "put"]
inputs = [[3], [1, 1], [2, 2], [2], [3, 5], [3, 3], [3], [2, 3]]

# exec(inputs, operations)


# recency_table = { 1: Node(1, 1) -> 2: Node(2, 2) -> 4: Node(3, 3)},  put (2, 3)
# Expected: recency_table = {1: Node(1, 1) -> 3: Node(2, 3) -> 4: Node(3, 3)}
operations = ["LFUCache", "put", "put",
              "get", "put", "get", "put", "get", "put"]
inputs = [[3], [1, 1], [2, 2], [2], [3, 5], [3], [3, 3], [3], [2, 3]]

# exec(inputs, operations)


# Wrong answer case
operations = ["LFUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put", "put", "get", "put",
              "put", "get", "put", "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
inputs = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [
    4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

exec(inputs, operations)
