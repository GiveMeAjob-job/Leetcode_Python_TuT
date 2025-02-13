# Leetcode_Python_TuT

Welcome to **Leetcode_Python_TuT** — a repository organizes and explains common **LeetCode** problems and solutions in **Python**, grouped by **Algorithmic Paradigm**, **Data Structure**, and additional **Techniques**. Below are quick links to each `.md` in the `docs/` folder.


Below, you’ll find links to subtopics. Each topic has its own `.md` file in the `docs/` folder, containing explanations and code samples:

---

## 1. Algorithmic Paradigms

All files are located under **`docs/algorithms/`**.

| Topic                                             | Description                                                                       |
|---------------------------------------------------|-----------------------------------------------------------------------------------|
| [Backtracking](docs/algorithms/backtracking.md)   | Explore all possible configurations (DFS/backtrack) for generating subsets, permutations, etc. |
| [Binary Search](docs/algorithms/binarysearch.md)  | Classic searching technique on sorted data; also “binary search on answers.”      |
| [Bitmask](docs/algorithms/bitmask.md)             | Enumerate subsets/states using bits; used for advanced DP or backtracking optimizations. |
| [Divide & Conquer](docs/algorithms/divide_and_conquer.md) | Split problems into subproblems (e.g., merge sort, quick sort, divide-and-conquer merges). |
| [DP (Dynamic Programming)](docs/algorithms/dp.md) | Solve overlapping subproblems with optimal substructure (knapsack, LCS, etc.).    |
| [Greedy](docs/algorithms/greedy.md)               | Make local optimal choices for a global optimum (interval scheduling, Huffman coding, etc.). |
| [Recursion](docs/algorithms/recursion.md)         | General recursive approaches, sometimes overlapping with backtracking or DP.      |
| [Sliding Window](docs/algorithms/slidingwindow.md)| Solve subarray/substring problems under certain conditions (max sum, min covering, etc.). |
| [Two Pointers](docs/algorithms/twopointers.md)    | Tackle array or string problems by moving pointers inward/outward (e.g., sums, partitioning). |

---

## 2. Data Structures

All files are located under **`docs/datastructures/`**.

| Topic                                                        | Description                                                                  |
|--------------------------------------------------------------|------------------------------------------------------------------------------|
| [Graph](docs/datastructures/graph.md)                       | Graph representations, BFS/DFS, shortest paths, topological sorting, etc.    |
| [Heap](docs/datastructures/heap.md)                         | Max/Min Heap, priority queues, heapify, and heap sort.                       |
| [Linked List](docs/datastructures/linkedlist.md)            | Singly/doubly linked lists, cycle detection, insertion/deletion, etc.        |
| [Monotonic Stack](docs/datastructures/monotonic_stack.md)   | A stack/queue that keeps elements in sorted order to solve “next greater element,” etc. |
| [Segment Tree](docs/datastructures/segmenttree.md)          | Range queries/updates (sum, min, max) in O(log n), plus Fenwick Tree (BIT).   |
| [Trees](docs/datastructures/trees.md)                       | Binary tree traversals, BST operations, tree-based DP, LCA, etc.             |
| [Union-Find](docs/datastructures/unionfind.md)              | Disjoint Set data structure for dynamic connectivity, MST, and grouping.      |

---

## 3. Techniques

All files are located under **`docs/techniques/`**.

| Topic                                                         | Description                                                                |
|---------------------------------------------------------------|----------------------------------------------------------------------------|
| [Bit Manipulation](docs/techniques/bit_manipulation.md)       | XOR, AND, OR, shifts, used for “unique elements,” subsets, tricky puzzle solutions. |
| [Math & Number Theory](docs/techniques/math_numbertheory.md)  | GCD, prime tests, combinatorics, modular arithmetic, etc.                 |
| [Sorting](docs/techniques/sorting.md)                         | Classic sorts (quick, merge, etc.) and sorting-based problem solutions.   |
| [String Algorithms](docs/techniques/string_algorithms.md)     | KMP, Rabin-Karp, Manacher’s, Trie structures, advanced string matching.   |

---

## Getting Started

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/GiveMeAjob-job/Leetcode_Python_TuT.git
   cd Leetcode_Python_TuT
   ```

2. (Optional) **Set up a virtual environment** and **install dependencies**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate         # Linux/Mac
   # or
   .\.venv\Scripts\activate          # Windows

   pip install -r requirements.txt
   ```

3. **Run code examples**:  
   - Navigate into a specific folder (e.g., `heap/`) and execute `python example_filename.py`.
   - Consult each `.md` file in `docs/` for more details about how the solutions and demos are structured.

## Project Structure

```
Leetcode_Python_TuT
├── README.md
└── docs
    ├── algorithms
    │   ├── backtracking.md
    │   ├── binarysearch.md
    │   ├── bitmask.md
    │   ├── divide_and_conquer.md
    │   ├── dp.md
    │   ├── greedy.md
    │   ├── recursion.md
    │   ├── slidingwindow.md
    │   └── twopointers.md
    ├── datastructures
    │   ├── graph.md
    │   ├── heap.md
    │   ├── linkedlist.md
    │   ├── monotonic_stack.md
    │   ├── segmenttree.md
    │   ├── trees.md
    │   └── unionfind.md
    ├── techniques
    │   ├── bit_manipulation.md
    │   ├── math_numbertheory.md
    │   ├── sorting.md
    │   └── string_algorithms.md
    └── ...
```

## Contributing

If you’d like to add new solutions, correct existing code, or enhance documentation, feel free to open an **Issue** or send a **Pull Request**. We appreciate all forms of collaboration.

Thank you for checking out **Leetcode_Python_TuT**. Happy coding!
