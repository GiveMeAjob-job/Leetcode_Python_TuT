#  Task B1: Initialize the MaxHeap Class
#  目标：搭建 MaxHeap 的基本结构；实现 __init__、top()、__len__() 等辅助方法。

class MaxHeap:
    def __init__(self):
        self.data = []

    def top(self):
        if not self.data:
            return None
        return self.data[0]

    def __len__(self):
        return len(self.data)

    #  Task B2: Implement the Push Operation (Insertion and Bubble Up)
    #  目标：完成插入操作，将新元素置于末尾并执行“上浮”以维护最大堆性质。

    def push(self, val):
        self.data.append(val)
        i = len(self.data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] > self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break


    #  Task B3: Implement the Pop Operation (Deletion and Bubble Down)
    #  目标：完成删除堆顶操作，用末尾元素补位并执行“下沉”以保持堆的“最大堆”特性。实现Bubble Down函数

    def _bubble_down(self, i):
        n = len(self.data)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2

            if left >= n:
                break

            child = left
            if right < n and self.data[right] > self.data[left]:
                child = right

            if self.data[i] >= self.data[child]:
                break

            self.data[i], self.data[child] = self.data[child], self.data[i]
            i = child




    def pop(self):
        if len(self.data) == 0:
            return None

        max_val = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()

        self._bubble_down(0)

        return max_val


heap = MaxHeap()
for x in [10,5,20,3,15,2]:
    heap.push(x)
print(heap.data)
print(heap.pop())  # 20
print(heap.pop())  # 15
print(heap.pop())  # 10
print(heap.pop())  # 5
print(heap.pop())  # 3
print(heap.pop())  # 2
print(heap.pop())  # None, 因为空了