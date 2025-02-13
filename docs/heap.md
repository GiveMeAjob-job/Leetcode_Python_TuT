# Heap (docs/heap.md)

A **Heap** is a special tree-based data structure, commonly used to maintain a **maximum** or **minimum** element efficiently. It supports:

- **Insert**: Add a new element and “bubble it up” to keep the heap property.
- **Delete/Extract Top**: Remove the root (maximum or minimum), then “bubble down” the new root so the heap property is preserved.
- **Build** or **heapify**: Convert an array into a heap in `O(n)` time by sifting elements from the bottom up.

## Why Use a Heap?

1. **Priority Queue**: Heaps provide a fast way (\( O(\log n) \)) to get or remove the top priority element (largest or smallest).  
2. **Sorting**: One can perform **Heap Sort** by building a heap, then repeatedly extracting the top element.  
3. **Scheduling & Resource Management**: The concept of “priority queues” is widely adopted in operating systems, event scheduling, or any scenario where the “highest priority” or “lowest cost” item must be retrieved first.

## Types of Heaps

1. **Max Heap**: The parent node is always greater or equal to its children, and the root is the maximum element in the heap.  
2. **Min Heap**: The parent node is always less or equal to its children, and the root is the minimum element in the heap.

In both cases, the heap is a **complete binary tree**, which allows efficient storage in an array with parent–child relationships determined by index arithmetic:
```
parent_index = (i - 1) // 2
left_child   = 2*i + 1
right_child  = 2*i + 2
```

## Key Operations

- **Push (Insert)**:  
  Place the new element at the end of the array (the “bottom” of the tree) and then “bubble up” if needed until the heap property is restored.

- **Pop (Extract Top)**:  
  Remove and return the root (which is either the maximum or the minimum), replace it with the last element in the array, and “bubble down” as necessary.

- **Heapify**:  
  Given an unsorted array, build a heap in `O(n)` time by sifting each non-leaf node from the bottom up.

## Examples & Code

We maintain a **MaxHeap** and a **MinHeap** implementation in the repository. You can find:

- **`MaxHeap`** code in [`heap/max_heap.py`](../heap/max_heap.py)  
- **`MinHeap`** code in [`heap/min_heap.py`](../heap/min_heap.py)

(**Note**: Adjust these paths according to your actual folder structure.)

### Quick Demo (Max Heap)

```python
from heap.max_heap import MaxHeap  # Example import

arr = [3, 1, 5, 2, 8, 10]
heap = MaxHeap()
for x in arr:
    heap.push(x)

print(heap.pop())  # Should output the max: 10
print(heap.pop())  # Next max: 8
# and so on...
```

## Further Reading

- **Heap Sort**: Using a heap to sort elements in `O(n log n)`.
- **Priority Queues**: Abstract data structure built on heaps for scheduling or event management.
- **Complexities**: 
  - Insertion / deletion from a heap: `O(log n)`  
  - Building a heap (heapify): `O(n)`

Feel free to explore additional examples under the [`heap/`](../heap/) directory.  
For broader context on binary trees, see [Trees](trees.md) and for advanced usage, check out the official Python `heapq` module in the standard library.
