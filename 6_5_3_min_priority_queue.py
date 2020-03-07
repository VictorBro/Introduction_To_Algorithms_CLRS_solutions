class MinPriorityQueue:

    def __init__(self, arr=None):
        self._heap = arr[:] if arr else []
        self._heap_size = len(self._heap)

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return (i * 2) + 1

    def _right(self, i):
        return (i * 2) + 2

    def _min_heapify(self, i):
        while True:
            l = self._left(i)
            r = self._right(i)
            smallest = i
            if l < self._heap_size and self._heap[i] > self._heap[l]:
                smallest = l
            if r < self._heap_size and self._heap[smallest] > self._heap[r]:
                smallest = r
            if smallest == i:
                break
            self._heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]
            i = smallest

    def minimum(self):
        return self._heap[0]

    def extract_min(self):
        if self._heap_size < 1:
            raise Exception("Heap is empty")
        min = self._heap[0]
        self._heap[0] = self._heap[self._heap_size - 1]
        self._heap_size -= 1
        self._min_heapify(0)
        return min

    def _shift_up(self, i):
        parent_idx = self._parent(i)
        while parent_idx >= 0 and self._heap[parent_idx] > self._heap[i]:
            self._heap[i], self._heap[parent_idx] = self._heap[parent_idx], self._heap[i]
            i = parent_idx
            parent_idx = self._parent(i)

    def _min_heap_insert(self, x):
        self._heap_size += 1
        if self._heap_size > len(self._heap):
            self._heap.append(x)
        else:
            self._heap[self._heap_size - 1] = x
        self._shift_up(self._heap_size - 1)

    def insert(self, x):
        self._min_heap_insert(x)

    def __str__(self):
        return str(self._heap[:self._heap_size])


def main():
    arr = [1, 2, 6, 4, 7, 8, 12, 5, 9, 13, 15]
    min_priority_queue = MinPriorityQueue(arr)
    min_priority_queue.insert(3)
    print(min_priority_queue)


if __name__ == "__main__":
    main()
