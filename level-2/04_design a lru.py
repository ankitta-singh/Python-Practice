class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def access(self, item):
        # If item already exists, remove it
        if item in self.cache:
            self.cache.remove(item)

        # If cache is full, remove least recently used item
        elif len(self.cache) == self.capacity:
            self.cache.pop(0)

        # Add new item as most recently used
        self.cache.append(item)

    def display(self):
        print("Cache:", self.cache)


# Driver Code
obj = LRUCache(3)

obj.access(1)
obj.display()

obj.access(2)
obj.display()

obj.access(3)
obj.display()

obj.access(2)
obj.display()

obj.access(4)
obj.display()
