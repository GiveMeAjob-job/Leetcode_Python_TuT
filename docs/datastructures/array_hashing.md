

---

| Status |LeetCode# | Title                             | Thought Process                                                                                                                                                |
|:----:|:------------:|:----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ ]  | 1            | Two Sum                           | Use a hash map to store values and their indices. For each element `nums[i]`, check if `target - nums[i]` is in the map.                                                                                             |
| [ ]  | 36           | Valid Sudoku                      | Use hash sets (or arrays) to track seen numbers in each row, column, and 3×3 box. Return false if any duplicate is found.                                                           |
| [ ]  | 49           | Group Anagrams                    | Sort each string or use a char frequency as a hash key, group strings by the same key in a hash map.                                                                                |
| [ ]  | 73           | Set Matrix Zeroes                 | First pass to find which rows and columns should be zero. Second pass to set them to zero. Can optimize with markers stored in the first row/column.                               |
| [ ]  | 128          | Longest Consecutive Sequence      | Put all numbers in a hash set. For each number, if `num - 1` not in set, then count how many consecutive numbers start from `num`. Track the max length.                            |
| [ ]  | 136          | Single Number                     | XOR all numbers; duplicates cancel out, leaving the unique number.                                                                                                                  |
| [ ]  | 137          | Single Number II                  | Each bit position accumulates how many times it appears modulo 3, reconstruct the single number. Alternatively, use bitwise operations/trick.                                      |
| [ ]  | 169          | Majority Element                  | Hash map to count frequency or use the Boyer-Moore Voting algorithm.                                                                                                                 |
| [ ]  | 219          | Contains Duplicate II             | Use a hash map or set sliding window to check if the same value reappears within k distance.                                                                                        |
| [ ]  | 220          | Contains Duplicate III            | Use a balanced tree structure / ordered map / bucket approach to check if any two elements within k distance are also within t difference.                                          |
| [ ]  | 238          | Product of Array Except Self      | Output array `res[i]` = product of all to the left * product of all to the right. You can do it in two passes without extra O(n) space for the right side.                          |
| [ ]  | 268          | Missing Number                    | XOR all indices with all values; the remainder is the missing number, or use sum formula `n*(n+1)/2 - sum(nums)`.                                                                    |
| [ ]  | 287          | Find the Duplicate Number         | Floyd’s Tortoise and Hare (cycle detection) in array indexes. Or use binary search on the range [1..n].                                                                             |
| [ ]  | 349          | Intersection of Two Arrays        | Use two hash sets. Put the elements of the first array in a set, then check the second array’s elements for membership.                                                             |
| [ ]  | 350          | Intersection of Two Arrays II     | Similar to #349 but need the intersection with frequency. Use a hash map to store counts, then decrement counts as you match elements in the second array.                         |
| [ ]  | 347          | Top K Frequent Elements           | Use a hash map to count frequency, then use a min-heap of size k, or use “bucket sort” approach if the range is large but the data size is not too big.                             |
| [ ]  | 525          | Contiguous Array                  | Transform 0 -> -1, accumulate prefix sum. Store the first index of each prefix sum in a hash map. If the same prefix sum reappears, subarray between them has equal 0/1.           |
| [ ]  | 560          | Subarray Sum Equals K             | Keep a running prefix sum. For each prefix sum `curr`, we check if `curr - k` exists in a hash map. The hash map counts how many times each prefix sum occurred.                  |
| [ ]  | 594          | Longest Harmonious Subsequence    | Use a hash map to count frequencies. The “harmonious” subsequence means elements differ by exactly 1. For each key, check `count[key] + count[key+1]`.                             |
| [ ]  | 697          | Degree of an Array                | Use a hash map to track frequency of each element, plus the first and last occurrence indices. The degree is max frequency, and you want the smallest subarray that achieves it.   |

---

