class HeapPriorityQueue:

    def __init__(self, arr=None):
        self._heap = arr[:] if arr else []
        self._heap_size = len(self._heap)

    def _parent(self, i):
        return (i - 1) // 2

    def _shift_up(self, i):
        parent_idx = self._parent(i)
        while parent_idx >= 0 and self._heap[parent_idx] < self._heap[i]:
            self._heap[i], self._heap[parent_idx] = self._heap[parent_idx], self._heap[i]
            i = parent_idx
            parent_idx = self._parent(i)

    def _max_heap_insert(self, x):
        self._heap_size += 1
        if self._heap_size > len(self._heap):
            self._heap.append(x)
        else:
            self._heap[self._heap_size - 1] = x
        self._shift_up(self._heap_size - 1)

    def insert(self, x):
        self._max_heap_insert(x)

    def __str__(self):
        return str(self._heap[:self._heap_size])


def main():
    arr = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    priority_queue = HeapPriorityQueue(arr)
    priority_queue.insert(10)
    print(priority_queue)


if __name__ == "__main__":
    main()
