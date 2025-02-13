#  Task D1：Initialize the MinHeap Class
#  目标：创建一个最小堆类 MinHeap，具备存储数组以及**top()、__len__()** 等基础方法，但尚未实现插入/删除。

class MinHeap:
    def __init__(self):
        self.data = []

    def top(self):
        """返回堆顶(最小值)，堆为空返回 None"""
        if not self.data:
            return None
        return self.data[0]

    def __len__(self):
        return len(self.data)

    # Task D2: Implement the Push Operation (Insertion and Bubble Up)
    #  目标：让 push 函数在插入值时，自动把它“上浮”到正确位置，保证“父节点 ≤ 子节点”。
    def push(self, val):
        self.data.append(val)
        i = len(self.data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    #  Task D3: Implement the Pop Operation (Deletion and Bubble Down
    #  目标：pop() 返回并删除最小值，也就是 self.data[0]。然后用末尾元素补到顶，并对它做下沉操作，维持“父 ≤ 子”的最小堆特性。
    def pop(self):
        if len(self.data) == 0:
            return None

        min_val = self.data[0]
        # 用最后一个元素顶替到下标0
        self.data[0] = self.data[-1]
        self.data.pop()  # 删除末尾
        self._bubble_down(0)
        return min_val

    def _bubble_down(self, i):
        n = len(self.data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2

            # 没有左孩子 => 没有孩子
            if left >= n:
                break

            # 选更小的孩子
            child = left
            if right < n and self.data[right] < self.data[left]:
                child = right

            # 如果当前节点 <= 更小孩子 => 不需交换
            if self.data[i] <= self.data[child]:
                break

            self.data[i], self.data[child] = self.data[child], self.data[i]
            i = child



h = MinHeap()
for x in [5,2,9,1,10]:
    h.push(x)

# 堆顶是1
print(h.pop())  # 1
print(h.pop())  # 2
print(h.pop())  # 5
print(h.pop())  # 9
print(h.pop())  # 10
print(h.pop())  # None (空堆)
