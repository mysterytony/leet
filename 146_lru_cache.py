class Node:
    key: int = 0
    val: int = 0
    lru = None  # less recently used
    mru = None  # more recently used


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lru = None
        self.mru = None
        self.size = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._cache_hit(key, self.cache[key].val)
        return self.cache[key].val

    def _cache_hit(self, key, new_value: int):
        hit = self.cache[key]
        hit.val = new_value
        if self.size == 1:
            return
        if self.mru == hit:
            return
        if hit.lru != None:
            hit.lru.mru = hit.mru
        if hit.mru != None:
            hit.mru.lru = hit.lru
        if self.lru == hit:
            self.lru = hit.mru
        if self.mru != None:
            self.mru.mru = hit
        hit.lru = self.mru
        hit.mru = None
        self.mru = hit

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._cache_hit(key, value)
        else:
            new = Node()
            new.val = value
            new.key = key
            new.mru = None
            new.lru = self.mru
            if self.mru != None:
                self.mru.mru = new
            self.mru = new
            self.cache[key] = new
            if self.lru == None:
                self.lru = new
            if self.size == self.cap:
                lru_temp = self.lru.mru
                del self.cache[self.lru.key]
                self.lru = lru_temp
                self.lru.lru = None
            else:
                self.size += 1
