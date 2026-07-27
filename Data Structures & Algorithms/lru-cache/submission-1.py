class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dct = {}
        self.max_cap = capacity
        self.cur_cap = 0
        self.LRU = Node(-1, 0)
        self.MRU = Node(-1, 0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def get(self, key: int) -> int:
        print(self.dct)
        if key in self.dct:
            self.remove(key)
            self.insert(key)
            return self.dct[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        print(self.dct)
        if key in self.dct:
            self.dct[key].value = value
            self.remove(key)
            self.insert(key)
        else:
            tmp = Node(key, value)
            self.dct[key] = tmp
            self.insert(key)

    def remove(self, key):
        node = self.dct[key]
        prev, next= node.prev, node.next
        prev.next = next
        next.prev = prev
        self.cur_cap -= 1
        
    
    def insert(self, key):
        node = self.dct[key]
        prev, next = self.MRU.prev, self.MRU
        prev.next = node
        next.prev = node
        node.next, node.prev = next, prev
        self.cur_cap += 1
        if self.cur_cap > self.max_cap:
            del_key = self.LRU.next.key
            self.remove(self.LRU.next.key)
            del self.dct[del_key]
            