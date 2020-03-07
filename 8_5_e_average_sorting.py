class HeapNode:
    def __init__(self, key, array_idx, key_idx, array_size):
        self.key = key
        self.array_idx = array_idx
        self.key_idx = key_idx
        self.array_size = array_size


def left(i):
    return (2 * i) + 1


def right(i):
    return (2 * i) + 2


class MinHeap:
    def __init__(self, A):
        self.heap = []
        self.heap_size = 0
        self.A = A
        self._build_min_heap()

    def _heapify(self, i):  # O(log k)
        while True:
            l = left(i)
            r = right(i)
            min_idx = i
            if l < self.heap_size and self.heap[min_idx].key > self.heap[l].key:
                min_idx = l
            if r < self.heap_size and self.heap[min_idx].key > self.heap[r].key:
                min_idx = r
            if min_idx == i:
                break
            self.heap[min_idx], self.heap[i] = self.heap[i], self.heap[min_idx]
            i = min_idx

    def _build_min_heap(self):  # O(k)
        self.heap_size = len(self.A)
        for i in range(self.heap_size):
            heap_node = HeapNode(self.A[i][0], i, 0, len(self.A[i]))
            self.heap.append(heap_node)
        start = (self.heap_size - 1) // 2
        for i in range(start, -1, -1):
            self._heapify(i)

    def extract_min(self):
        if self.heap_size <= 0:
            raise Exception("heap underflow")

        heap_node = self.heap[0]
        if heap_node.key_idx + 1 < heap_node.array_size:
            new_heap_node = HeapNode(self.A[heap_node.array_idx][heap_node.key_idx + 1],
                                     heap_node.array_idx,
                                     heap_node.key_idx + 1,
                                     heap_node.array_size)
            self.heap[0] = new_heap_node
        else:
            self.heap[0] = self.heap[self.heap_size - 1]
            self.heap_size -= 1

        self._heapify(0)
        return heap_node.key


def k_merge(A, start, end, step):
    heap_array = []
    for i in range(start, end + 1, step):
        temp = []
        for j in range(i, i + step):
            if j <= end:
                temp.append(A[j])
        heap_array.append(temp)
    print(heap_array)  # delete
    min_heap = MinHeap(heap_array)
    for i in range(start, end + 1):
        A[i] = min_heap.extract_min()


def k_merge_sort(A, k, start, end):
    if start < end:
        step = -(-(end - start + 1) // k)
        for i in range(start, end + 1, step):
            local_end = i + step - 1
            if local_end > end:
                local_end = end
            k_merge_sort(A, k, i, local_end)  # T(n/k)
        print("step=", step)  # delete
        k_merge(A, start, end, step)  # O(n/k * log(k))
        print(A)


def k_sort(A, k):
    n = len(A)
    for i in range(k):  # O(k)
        print("\nround=", i)  # delete
        if i < n:
            start = i
        end = start + ((n - 1) // k)*k
        if end >= n:
            end -= k
        sub_array = A[start:end+1:k]  # O(N/k)
        print(sub_array)  # delete
        sub_array_len = len(sub_array)
        k_merge_sort(sub_array, k, 0, sub_array_len - 1)
        for j in range(sub_array_len):  # O(N/k)
            A[start + (j * k)] = sub_array[j]


def main():
    # A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    k_sort(A, 3)  # O(k*T(N/k))
    print(A)


if __name__ == "__main__":
    main()
