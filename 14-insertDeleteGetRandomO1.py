class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.data = [] 

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False

        self.hashmap[val] = len(self.data)
        self.data.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        if not val in self.hashmap:
            return False

        last_el = self.data[-1]
        idx = self.hashmap[val]

        self.hashmap[last_el] = idx
        self.data[idx] = last_el

        self.data[-1] = val
        self.data.pop()

        self.hashmap.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)