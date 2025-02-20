class Set:
    def __init__(self, elements=None):
        self.set = []
        if elements is not None:
            for element in elements:
                self.add(element)

    def add(self, value):
        if not self.contains(value):
            new_set = [0] * (len(self.set) + 1)
            for i in range(len(self.set)):
                new_set[i] = self.set[i]
            new_set[len(self.set)] = value
            self.set = new_set

    def contains(self, value):
        for element in self.set:
            if element == value:
                return True
        return False

    def remove(self, value):
        if not self.contains(value):
            raise ValueError(f"{value} not in set")
        new_set = [0] * (len(self.set) - 1)
        j = 0
        for i in range(len(self.set)):
            if self.set[i] != value:
                new_set[j] = self.set[i]
                j += 1
        self.set = new_set

    def union(self, other_set):
        result = Set(self.set)
        for element in other_set.set:
            result.add(element)
        return result

    def intersection(self, other_set):
        result = Set()
        for element in self.set:
            if other_set.contains(element):
                result.add(element)
        return result

    def difference(self, other_set):
        result = Set()
        for element in self.set:
            if not other_set.contains(element):
                result.add(element)
        return result

    def is_subset(self, other_set):
        for element in self.set:
            if not other_set.contains(element):
                return False
        return True