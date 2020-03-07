class HeapNode:

    def __init__(self, key, i, next_idx):
        self.key = key
        self.i = i
        self.next_idx = next_idx


def left(i):
    return (i * 2) + 1


def right(i):
    return (i * 2) + 2


def parent(i):
    return (i - 1) // 2


class MinHeap:

    def __init__(self, heap_nodes):
        self._heap_size = len(heap_nodes)
        self._heap = heap_nodes
        self._build_min_heap()

    def _heapify(self, i):
        while True:
            l = left(i)
            r = right(i)
            smallest = i
            if l < self._heap_size and self._heap[i].key > self._heap[l].key:
                smallest = l
            if r < self._heap_size and self._heap[smallest].key > self._heap[r].key:
                smallest = r
            if smallest == i:
                break
            self._heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]
            i = smallest

    def _build_min_heap(self):
        start = (self._heap_size - 1) // 2
        for i in range(start, -1, -1):
            self._heapify(i)

    def extract_min(self):
        if self._heap_size < 1:
            print("Heap underflow")
            return None
        min_key = self._heap[0]
        self._heap[0] = self._heap[self._heap_size - 1]
        self._heap_size -= 1
        self._heapify(0)
        return min_key

    def _shift_up(self, i):
        parent_idx = parent(i)
        temp = self._heap[i]
        while parent_idx >= 0 and self._heap[parent_idx].key > temp.key:
            self._heap[i] = self._heap[parent_idx]
            i = parent_idx
            parent_idx = parent(i)
        self._heap[i] = temp

    def insert(self, heap_node):
        self._heap_size += 1
        if self._heap_size > len(self._heap):
            self._heap.append(heap_node)
        else:
            self._heap[self._heap_size - 1] = heap_node
        self._shift_up(self._heap_size - 1)

    def size(self):
        return self._heap_size

    def __str__(self):
        return str([self._heap[i].key for i in range(self._heap_size)])


def merge_sorted_lists(sorted_lists):
    k = len(sorted_lists)
    sorted_list_size = len(sorted_lists[0])
    n = k * sorted_list_size
    result = []
    heap_nodes = []

    for i in range(k):  # O(k)
        if len(sorted_lists[i]) > 0:
            heap_node = HeapNode(sorted_lists[i][0], i, 1)
            heap_nodes.append(heap_node)

    min_heap = MinHeap(heap_nodes)  # O(k)

    while min_heap.size() > 0:  # O(n * log k)
        min_key = min_heap.extract_min()  # O(log k)
        if min_key is None:
            break
        result.append(min_key.key)
        if min_key.next_idx < len(sorted_lists[min_key.i]):
            heap_node = HeapNode(sorted_lists[min_key.i][min_key.next_idx], min_key.i, min_key.next_idx + 1)
            min_heap.insert(heap_node)  # O(log k)

    return result


def main():
    # sorted_lists = [[2, 6, 12, 34],
    #                 [1, 9, 20, 1000],
    #                 [23, 34, 90, 2000]]
    # sorted_lists = [[1, 2, 3, 4, 5],
    #                 [2, 2, 2, 2, 2],
    #                 [1, 1, 1, 1, 1]]
    # sorted_lists = [[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]]
    sorted_lists = [[]]

    result = merge_sorted_lists(sorted_lists)
    print(result)


if __name__ == "__main__":
    main()
