class Array:
    def __init__(self, initial_list=None):
        self.arr = initial_list if initial_list is not None else []

    def append(self, value):
        new_arr = [0] * (len(self.arr) + 1)
        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        new_arr[len(self.arr)] = value
        self.arr = new_arr

    def insert(self, index, value):
        new_arr = [0] * (len(self.arr) + 1)
        for i in range(len(self.arr) + 1):
            if i < index:
                new_arr[i] = self.arr[i]
            elif i == index:
                new_arr[i] = value
            else:
                new_arr[i] = self.arr[i - 1]
        self.arr = new_arr

    def remove(self, value):
        new_arr = [0] * (len(self.arr) - 1)
        found = False
        j = 0
        for i in range(len(self.arr)):
            if not found and self.arr[i] == value:
                found = True
                continue
            if j < len(new_arr):
                new_arr[j] = self.arr[i]
                j += 1
        if not found:
            raise ValueError(f"{value} not in list")
        self.arr = new_arr

    def pop(self, index=-1):
        if index < 0:
            index += len(self.arr)
        if index >= len(self.arr) or index < 0:
            raise IndexError("pop index out of range")
        value = self.arr[index]
        self.remove(value)
        return value

    def sort(self, reverse=False):
        for i in range(len(self.arr)):
            for j in range(i + 1, len(self.arr)):
                if (self.arr[i] > self.arr[j]) != reverse:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def reverse(self):
        n = len(self.arr)
        for i in range(n // 2):
            self.arr[i], self.arr[n - i - 1] = self.arr[n - i - 1], self.arr[i]

    def index(self, value):
        for i in range(len(self.arr)):
            if self.arr[i] == value:
                return i
        raise ValueError(f"{value} not in list")

    def count(self, value):
        count = 0
        for item in self.arr:
            if item == value:
                count += 1
        return count

    def slice(self, start=None, end=None, step=1):
        result = []
        start = start if start is not None else 0
        end = end if end is not None else len(self.arr)
        for i in range(start, end, step):
            result.append(self.arr[i])
        return result


