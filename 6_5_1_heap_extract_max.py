class HeapPriorityQueue:

    def __init__(self, arr=None):
        self._heap = arr[:] if arr else []
        self._heap_size = len(self._heap)

    def _left(self, i):
        return (2 * i) + 1

    def _right(self, i):
        return (2 * i) + 2

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

    def _heap_extract_max(self):
        if self._heap_size < 1:
            raise Exception("Heap is empty")
        max_val = self._heap[0]
        self._heap[0] = self._heap[self._heap_size - 1]
        self._heap_size -= 1
        self._heapify(0)
        return max_val

    def extract_max(self):
        return self._heap_extract_max()

    def __str__(self):
        return str(self._heap[:self._heap_size])


def main():
    arr = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    priority_queue = HeapPriorityQueue(arr)
    max_val = priority_queue.extract_max()
    print(max_val)
    print(priority_queue)


if __name__ == "__main__":
    main()
