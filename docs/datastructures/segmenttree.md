
---

| Status | LeetCode# | Title                                    | Thought Process                                                                                                                                        |
|:----:|:------------:|:-----------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ ]  | 307          | Range Sum Query - Mutable                | Build a Segment Tree to support both updating an element and querying the sum of a range. Fenwick Tree is also an alternative.                                                                                  |
| [ ]  | 308          | Range Sum Query 2D - Mutable             | 2D version of segment tree. Allows updating a cell and querying sum over any sub-rectangle. More complex to implement, but the concept is similar to 1D segment tree.                                           |
| [ ]  | 315          | Count of Smaller Numbers After Self      | Can be solved with a Segment Tree or Fenwick Tree that compresses and counts how many numbers have appeared. As you iterate from right to left (or left to right), you query how many are smaller.              |
| [ ]  | 327          | Count of Range Sum                       | After computing prefix sums, use a Segment Tree / Fenwick Tree to count how many prefix sums fall within a certain range. (Alternatively mergesort or balanced BST approach, but segment tree is one option.)   |
| [ ]  | 699          | Falling Squares                          | Track intervals (the squares) along the x-axis. Use a segment tree to record and update the maximum height in any interval, so you can place new squares and update the global maximum.                         |
| [ ]  | 715          | Range Module                             | A segment tree or balanced tree can be used to maintain intervals of “covered” segments. Supports operations like addRange, removeRange, queryRange.                                                             |
| [ ]  | 731          | My Calendar II                           | Keep track of room bookings (start/end times). Use a segment tree or sweep line. The segment tree can store how many bookings overlap in each segment.                                                           |
| [ ]  | 732          | My Calendar III                          | Similar to #731 but we need the maximum number of concurrent events. A segment tree node can hold the count of how many events overlap and track the maximum overlap in that segment.                           |
| [ ]  | 1649         | Create Sorted Array Through Instructions | As you process each element, you want to know how many smaller/greater have appeared. Use a segment/fenwick tree for counting. The cost is the min of placing it “left” or “right.”                             |

---

