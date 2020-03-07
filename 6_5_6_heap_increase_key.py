class MaxPriorityQueue:

    def __init__(self, arr=None):
        self._heap = arr[:] if arr else []
        self._heap_size = len(self._heap)

    def _parent(self, i):
        return (i - 1) // 2

    def heap_increase_key(self, i, key):
        if key < self._heap[i]:
            raise Exception("New key is smaller than current key")
        parent_idx = self._parent(i)
        while parent_idx >= 0 and self._heap[parent_idx] < key:
            self._heap[i] = self._heap[parent_idx]
            i = parent_idx
            parent_idx = self._parent(i)
        self._heap[i] = key

    def __str__(self):
        return str(self._heap[:self._heap_size])


def main():
    arr = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1, 10]
    max_priority_queue = MaxPriorityQueue(arr)
    max_priority_queue.heap_increase_key(len(arr) - 1, 9)
    print(max_priority_queue)


if __name__ == "__main__":
    main()
