from MaxHeap import MaxHeap
#  Task C1: Naive Heap Construction with Repeated Push
#  理解最朴素的建堆方式：把数组中每个元素依次 push 到你已有的 MaxHeap 中。

def build_heap_naive(arr):
    heap = MaxHeap(arr)
    for x in arr:
        heap.push(x)
    return heap

#  Task C2: Efficient Heapify in O(n)
#  实现真正的heapify：从无序数组开始，一次性把它变成一个最大堆。
#  掌握自底向上、下沉 (bubble down)的做法，让算法整体在 O(N)时间内完成

def heapify(arr):
    mh = MaxHeap()
    """把arr变成一个最大堆存到self.data里"""
    mh.data = arr[:]
    n = len(mh.data)
    #  从最后一个非叶子节点往回走
    #  (i.e. i = n//2 - 1 down to 0)
    for i in range(n//2 - 1, -1, -1):
        mh._bubble_down(i)
    return mh

arr = [3,1,5,2,8,10]
heap = heapify(arr)      # 一次性建堆
while len(heap) > 0:
    print(heap.pop(), end=" ")