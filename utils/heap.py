class Heap:
    def __init__(self, comparator):
        self.comparator = comparator
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        child = self.size()
        parent = self.get_parent(child)
        self.data.append(item)
        while parent is not None:
            if self.comparator(self.data[child], self.data[parent]):
                self.data[child], self.data[parent] = self.data[parent], self.data[child]
                child = parent
                parent = self.get_parent(child)
            else:
                parent = None
        return self.size()

    def pop(self):
        if self.size() > 0:
            self.data[0], self.data[self.size() - 1] = self.data[self.size() - 1], self.data[0]
            result = self.data.pop()
            self.sift_down(0)
            return result

    def get_right_child(self, parent):
        child = (parent * 2) + 2
        if 0 <= child < self.size():
            return child

    def get_left_child(self, parent):
        child = (parent * 2) + 1
        if 0 <= child < self.size():
            return child

    def get_parent(self, child):
        parent = (child - 1) // 2

        if 0 <= parent < self.size():
            return parent

    def sift_down(self, parent):
        while parent is not None:
            left_child = self.get_left_child(parent)
            right_child = self.get_right_child(parent)

            if left_child is not None and right_child is not None:
                if self.comparator(self.data[left_child], self.data[right_child]):
                    child = left_child
                else:
                    child = right_child
            elif left_child is not None:
                child = left_child
            elif right_child is not None:
                child = right_child
            else:
                return

            if not self.comparator(self.data[parent], self.data[child]):
                self.data[parent], self.data[child] = self.data[child], self.data[parent]
                parent = child
            else:
                parent = None