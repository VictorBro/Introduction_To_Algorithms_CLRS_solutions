class Stack:
    def __init__(self):
        self.n = 10
        self.arr = [9] * self.n
        self.top = -1

    def push(self, k):
        if self.top == self.n:
            raise Exception("overflow")
        self.top += 1
        self.arr[self.top] = k

    def pop(self):
        if self.top == -1:
            raise Exception("underflow")
        ret = self.arr[self.top]
        self.top -= 1
        return ret


class Dict:
    def __init__(self):
        self.n = 10
        self.arr = [8] * self.n
        self.stack = Stack()

    def insert(self, k):
        pointer_to_arr = k
        self.stack.push(pointer_to_arr)
        pointer_to_stack = self.stack.top
        self.arr[k] = pointer_to_stack

    def delete(self, k):
        pointer_to_stack = self.arr[k]
        pointer_to_arr = self.stack.pop()
        if pointer_to_stack <= self.stack.top:
            self.stack.arr[pointer_to_stack] = pointer_to_arr
            self.arr[pointer_to_arr] = pointer_to_stack

    def search(self, k):
        pointer_to_stack = self.arr[k]
        if self.stack.arr[pointer_to_stack] == k:
            return True
        else:
            return False

    def __str__(self):
        return str(self.stack.arr) + "\n" + str(self.arr)


def main():
    mydict = Dict()
    print(mydict)
    mydict.insert(3)
    print("insert 3")
    print(mydict)
    mydict.insert(5)
    print("insert 5")
    print(mydict)
    mydict.insert(9)
    print("insert 9")
    print(mydict)
    print(mydict.search(9))
    print(mydict)
    print(mydict.search(8))
    print(mydict)
    mydict.delete(5)
    print("delete 5")
    print(mydict)
    print(mydict.stack.top)


if __name__ == "__main__":
    main()
