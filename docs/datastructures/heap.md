# Heap (docs/heap.md)
| Status | LeetCode# | Title                                         | Thought Process                                                                                                                                                            |
|-------:|----------:|:----------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |       215 | Kth Largest Element in an Array               | Use a **min-heap** of size k. Push elements into the heap, and if the heap size exceeds k, pop the smallest. The heap top is the kth largest element.                      |
|        |       347 | Top K Frequent Elements                       | Count frequencies. Use a **min-heap** of size k based on frequency. Keep top k frequent elements in the heap.                                                              |
|        |       703 | Kth Largest Element in a Stream               | Maintain a **min-heap** of size k for the incoming stream. For each new number, push it in; if heap size > k, pop the smallest. The top is always the kth largest.         |
|        |        23 | Merge k Sorted Lists                          | Use a **min-heap** to keep track of the heads of each list. Repeatedly pop the smallest node and push its next node into the heap until all lists are merged.              |
|        |       295 | Find Median from Data Stream                  | Maintain two heaps: a **max-heap** for the lower half, and a **min-heap** for the upper half. Balance their sizes so the median can be easily found from the tops.         |
|        |       378 | Kth Smallest Element in a Sorted Matrix       | Use a **min-heap**. Insert the first element of each row, pop the smallest, then insert the next element from that row. Do this k times to find the kth smallest.          |
|        |       692 | Top K Frequent Words                          | Similar to #347 but for words. Use a **min-heap** of size k by frequency, and if frequencies tie, sort by lexicographical order.                                           |
|        |      1046 | Last Stone Weight                             | Use a **max-heap** of stone weights. Repeatedly pop two largest, smash them, and if there is a remainder, push it back. Continue until ≤1 stone remains.                   |
|        |       973 | K Closest Points to Origin                    | Use a **max-heap** of size k. For each point, calculate distance to origin, push it. If heap size exceeds k, pop the largest.                                              |
|        |       264 | Ugly Number II                                | Use a **min-heap** to generate ugly numbers. Pop the smallest and generate its multiples by 2, 3, 5; avoid duplicates. The nth popped is the nth ugly number.              |
|        |       621 | Task Scheduler                                | Use a **max-heap** of tasks by frequency. Repeatedly schedule the most frequent task, track cooldown, and then re-push tasks when they become available.                   |
|        |       767 | Reorganize String                             | Use a **max-heap** of characters by frequency. Pop the top two distinct chars in turn to build the result string so no two adjacent chars are the same.                    |
|        |       502 | IPO                                           | Use a **max-heap** of project profits that are affordable with current capital. Pick the largest profit project each time until you've done k projects or none left.       |
|        |       632 | Smallest Range Covering Elements from K Lists | Use a **min-heap** of the current elements (one from each list). Track the current max of these elements. Pop the smallest and push the next element of that list.         |
|        |      1642 | Furthest Building You Can Reach               | Use a **max-heap** (or min-heap in some implementations) to manage climbs. Whenever you exceed the available bricks, consider using a ladder for the highest climb.        |
|        |      1834 | Single-Threaded CPU                           | Sort tasks by arrival time. Push available tasks into a **min-heap** by their processing time. The CPU always picks the smallest processing time task available to run.    |

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

- **`MaxHeap`** code in [`heap/max_heap.py`](../Data%20Structures/heap/max_heap.py)  
- **`MinHeap`** code in [`heap/min_heap.py`](../Data%20Structures/heap/min_heap.py)

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

Feel free to explore additional examples under the [`heap/`](../Data%20Structures/heap/) directory.  
For broader context on binary trees, see [Trees](trees.md) and for advanced usage, check out the official Python `heapq` module in the standard library.
