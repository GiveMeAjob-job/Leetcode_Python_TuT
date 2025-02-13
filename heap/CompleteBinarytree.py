from collections import deque

temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#  Task A1: Compute Tree Levels
#  目标：根据数组长度或其他方法，计算它所表示的“完全二叉树”有多少层（或高度）。

def computetreelevels(arr:list):
    n = len(arr)
    level = 0
    while n > 0:
        n = n//2
        level = level + 1
    return level

print(computetreelevels(temp))


#  Task A2: Print TreeBy Levels
#  目标：打印数组所有的完全二叉树节点，从根节点到最后一层，每层输出相应的元素。


def getchildrenvalues(arr: list) -> list:
    if not arr:  # 检查空输入
        return []

    level = computetreelevels(arr)
    result = []

    for L in range(level):
        start = 2 ** L - 1  # 该层起始下标
        end = 2 ** (L + 1) - 2  # 该层结束下标

        # 如果超出数组长度，就停止
        if start >= len(arr):
            break

        # 保证不越界
        end = min(end, len(arr) - 1)

        # 从arr中提取本层节点
        layer_nodes = arr[start: end + 1]
        result.append(layer_nodes)

    return result

print(getchildrenvalues(temp))


#  Task A3: Get Children Values
#  目标：给定数组和节点索引 i，根据完全二叉树的特性，返回它的左右孩子的值（若存在）。

def getsthechildrenvalues(arr:list, nodeindex: int) -> list:
    if not arr or nodeindex < 0 or nodeindex >= len(arr):
        return []

    left_index = 2 * nodeindex + 1
    right_index = 2 * nodeindex + 2

    result = []

    if left_index < len(arr):
        result.append(arr[left_index])
    if right_index < len(arr):
        result.append(arr[right_index])

    return result

print(getsthechildrenvalues(temp, 5))

#  Task A4: Get Children Values
#  目标：给定数组和节点索引 i，根据完全二叉树的特性，返回它本身的值和它左右孩子的值（若存在）。

def getchildrenvalues(arr:list, nodeindex: int) -> list:
    if not arr or nodeindex < 0 or nodeindex >= len(arr):
        return []

    result = []
    q = deque([nodeindex])

    while q:
        size = len(q)
        level_nodes = []

        for i in range(size):
            idx = q.popleft()
            level_nodes.append(arr[idx])

            left_index = 2 * idx + 1
            right_index = 2 * idx + 2

            if left_index < len(arr):
                q.append(left_index)
            if right_index < len(arr):
                q.append(right_index)

        result.append(level_nodes)

    return result

print(getchildrenvalues(temp, 5))






