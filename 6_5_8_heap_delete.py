class Heap:
    def __init__(self, arr=None):
        self._heap = arr[:] if arr else []
        self._heap_size = len(self._heap)

    def _left(self, i):
        return (i * 2) + 1

    def _right(self, i):
        return (i * 2) + 2

    def _parent(self, i):
        return (i - 1) // 2

    def _heapify(self, i):
        while True:
            l = self._left(i)
            r = self._right(i)
            largest = i
            if l < self._heap_size and self._heap[i] < self._heap[l]:
                largest = l
            if r < self._heap_size and self._heap[largest] < self._heap[r]:
                largest = r
            if largest == i:
                break
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            i = largest

    def _shift_up(self, i):
        parent_idx = self._parent(i)
        temp = self._heap[i]
        while parent_idx >= 0 and self._heap[parent_idx] < temp:
            self._heap[i] = self._heap[parent_idx]
            i = parent_idx
            parent_idx = self._parent(i)
        self._heap[i] = temp

    def heap_delete(self, i):
        temp = self._heap[i]
        self._heap[i] = self._heap[self._heap_size - 1]
        self._heap_size -= 1
        if self._heap[i] >= temp:
            self._shift_up(i)
        else:
            self._heapify(i)

    def __str__(self):
        return str(self._heap[:self._heap_size])


def main():
    arr = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    heap = Heap(arr)
    heap.heap_delete(1)
    print(heap)

    arr = [13, 7, 12, 5, 6, 11]
    heap = Heap(arr)
    heap.heap_delete(4)
    print(heap)


if __name__ == "__main__":
    main()
