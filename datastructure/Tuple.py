class Tuple:
    def __init__(self, *args):
        self.elements = [arg for arg in args]

    def get(self, index):
        if index < 0 or index >= len(self.elements):
            raise IndexError("tuple index out of range")
        return self.elements[index]

    def length(self):
        count = 0
        for _ in self.elements:
            count += 1
        return count

    def index(self, value):
        for i in range(self.length()):
            if self.elements[i] == value:
                return i
        raise ValueError(f"{value} not in tuple")

    def count(self, value):
        count = 0
        for item in self.elements:
            if item == value:
                count += 1
        return count

    def to_list(self):
        new_list = [0] * self.length()
        for i in range(self.length()):
            new_list[i] = self.elements[i]
        return new_list



