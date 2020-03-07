class DaryHeap:
    def __init__(self, arr, d):
        self._heap = arr
        self._heap_size = len(arr)
        self._d = d
        self._build_max_heap()

    def _d_ary_child(self, i, nth_child):
        return (i * self._d) + nth_child + 1

    def _d_ary_parent(self, i):
        return (i - 1) // self._d

    def _heapify(self, i):
        largest = i
        while True:
            for pos in range(self._d):
                child_idx = self._d_ary_child(i, pos)
                if child_idx < self._heap_size and self._heap[child_idx] > self._heap[largest]:
                    largest = child_idx
            if largest == i:
                break
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            i = largest

    def _build_max_heap(self):
        start = self._d_ary_parent(self._heap_size - 1)
        for i in range(start, -1, -1):
            self._heapify(i)

    def extract_max(self):
        if self._heap_size < 1:
            print("heap underflow")
            return None
        max_key = self._heap[0]
        self._heap[0] = self._heap[self._heap_size - 1]
        self._heap_size -= 1
        self._heapify(0)
        return max_key

    def _shift_up(self, i):
        parent_idx = self._d_ary_parent(i)
        temp = self._heap[i]
        while parent_idx >= 0 and self._heap[parent_idx] < temp:
            self._heap[i] = self._heap[parent_idx]
            i = parent_idx
            parent_idx = self._d_ary_parent(i)
        self._heap[i] = temp

    def increase_key(self, i, key):
        if key < self._heap[i]:
            raise Exception("new key is smaller than current key")
        parent_idx = self._d_ary_parent(i)
        while parent_idx >= 0 and self._heap[parent_idx] < key:
            self._heap[i] = self._heap[parent_idx]
            i = parent_idx
            parent_idx = self._d_ary_parent(i)
        self._heap[i] = key

    def insert(self, x):
        self._heap_size += 1
        if self._heap_size > len(self._heap):
            self._heap.append(x)
        else:
            self._heap[self._heap_size - 1] = x
        self._shift_up(self._heap_size - 1)

    def __str__(self):
        return str(self._heap[:self._heap_size])


def main():
    arr = [6, 7, 8, 9, 12, 11, 13, 4, 5]
    max_heap = DaryHeap(arr, 3)
    print(max_heap)
    print(max_heap.extract_max())
    print(max_heap)
    max_heap.insert(13)
    print(max_heap)
    max_heap.increase_key(5, 12)
    print(max_heap)
    max_heap.increase_key(5, 10)


if __name__ == "__main__":
    main()
