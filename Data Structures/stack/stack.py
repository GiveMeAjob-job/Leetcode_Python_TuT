#  LeetCode 155
#  Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#  Implement the MinStack class:
#
#  MinStack() initializes the stack object.
#  void push(int val) pushes the element val onto the stack.
#  void pop() removes the element on the top of the stack.
#  int top() gets the top element of the stack.
#  int getMin() retrieves the minimum element in the stack.
#  You must implement a solution with O(1) time complexity for each function.
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 如果 min_stack 为空 或 新元素 <= min_stack栈顶，则压入 min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            # 如果弹出的元素等于 min_stack 的栈顶，则把 min_stack 同步弹出
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # 如果 stack 不为空就返回栈顶
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # 返回 min_stack 栈顶
        return self.min_stack[-1] if self.min_stack else None


# 创建 MinStack 实例
minStack = MinStack()

# 通过实例调用方法
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # 输出最小值
minStack.pop()
print(minStack.top())  # 输出栈顶元素
print(minStack.getMin())  # 输出最小值


#  LeetCode 739
#  Given an array of integers temperatures represents the daily temperatures,
#  return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
#  If there is no future day for which this is possible, keep answer[i] == 0 instead.
#  Example 1:
#  Input: temperatures = [73,74,75,71,69,72,76,73]
#  Output: [1,1,4,2,1,1,0,0]
#  Example 2:
#  Input: temperatures = [30,40,50,60]
#  Output: [1,1,1,0]
#  Example 3:
#  Input: temperatures = [30,60,90]
#  Output: [1,1,0]
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = []


