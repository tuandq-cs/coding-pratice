class Item:
    key: int
    value: int

    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value


class Pointer:
    def __init__(self, item: Item) -> None:
        self.item = item
        self.prev_pointer = None
        self.next_pointer = None


class LinkedList:
    __head: Pointer
    __tail: Pointer or None

    def __init__(self) -> None:
        self.__head = Pointer(item=Item(-1, -1))
        self.__tail = self.__head

    def append(self, p: Pointer):
        p.prev_pointer = self.__tail
        self.__tail.next_pointer = p
        p.next_pointer = None
        self.__tail = p

    def pop_head(self) -> Item or None:
        if self.__head.next_pointer is None:
            return None
        lru_pointer = self.__head.next_pointer
        next_lru_pointer = lru_pointer.next_pointer
        if next_lru_pointer is None:  # lru is tail
            self.__tail = self.__head
        else:
            next_lru_pointer.prev_pointer = self.__head
        self.__head.next_pointer = next_lru_pointer
        return lru_pointer.item

    def remove_pointer(self, p: Pointer):
        if p == self.__tail:
            self.__tail = self.__tail.prev_pointer
            return
        prev_p = p.prev_pointer
        prev_p.next_pointer = p.next_pointer
        p.next_pointer.prev_pointer = prev_p

    def show(self):
        cur_p = self.__head.next_pointer
        while (cur_p is not None):
            print(cur_p.item.key, cur_p.item.value)
            cur_p = cur_p.next_pointer


class LRUCache:
    __capacity: int
    __table: dict[int, Pointer]
    __age_linked_list: LinkedList

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__table = {}
        self.__age_linked_list = LinkedList()

    def get(self, key: int) -> int:
        if self.__table.get(key) is None:
            return -1
        p = self.__table[key]
        # Remove it from age linked list
        self.__age_linked_list.remove_pointer(p)
        # Append it to the end of linked list
        self.__age_linked_list.append(p)
        return p.item.value

    def put(self, key: int, value: int) -> None:
        if self.__table.get(key) is not None:
            # Update table
            p = self.__table[key]
            p.item.value = value
            # Remove it from age linked list
            self.__age_linked_list.remove_pointer(p)
            # Append it to the end of linked list
            self.__age_linked_list.append(p)
        else:
            if len(self.__table) == self.__capacity:
                # Pop LRU item from linked list
                lru_item = self.__age_linked_list.pop_head()  # Time: O(1)
                # Remove LRU item from table
                del self.__table[lru_item.key]
            # Append new item to table, linked lists
            p = Pointer(item=Item(key, value))
            self.__table[key] = p
            self.__age_linked_list.append(p)

    def show(self):
        self.__age_linked_list.show()
        print(self.__table.keys())

# Corner case
# Capacity = 1


capacity = 1
obj = LRUCache(capacity)
inputs = [[1, 1], [1], [2, 2], [2, 3], [2]]
ops = ["put", "get", "put", "put", "get"]
# Capacity = 1
# Table = {
#   2: Pointer(2,3)
# }
# Linked_list: Head = Pointer(-1, -1) <-> Pointer(2, 3) = Tail

for i, op in enumerate(ops):
    print('i', i, ', op', op, 'input', inputs[i])
    if op == "put":
        key, value = inputs[i]
        obj.put(key, value)
        # print("null")
    else:
        key = inputs[i][0]
        # obj.get(key)
        print(obj.get(key))

capacity = 10
obj = LRUCache(capacity)
inputs = [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [
    4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
for i, op in enumerate(["put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
                       ):
    print('i', i, ', op', op, 'input', inputs[i])
    if op == "put":
        key, value = inputs[i]
        obj.put(key, value)
        # print("null")
    else:
        key = inputs[i][0]
        # obj.get(key)
        print(obj.get(key))
    # obj.show()

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# Capacity = 2
# prev = tail

# Table = {
#   3: Pointer(3, 3)
#   4: Pointer(4, 4)
# }
# Linked_list: Head = Pointer(-1, -1) <-> Pointer(3, 3) <-> Pointer(4, 4) = Tail
# Put [1, 1]
# Put [2, 2]
# Get [1] -> 1
# Put [3, 3]
# Get [2] -> -1
# Put [4, 4]
# Get [1] -> -1
# Get [3] -> 3
# Get [4] -> 4
