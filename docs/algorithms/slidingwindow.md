
---

| Status | LeetCode# | Title                                          | Thought Process                                                                                                                                                                   |
|:------:|:---------:|:-----------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   ✅    |     3     | Longest Substring Without Repeating Characters | Use a sliding window with a hash/dictionary to track characters and their indices. Expand right pointer, if a duplicate appears, move left pointer to shrink the window.          |
|  [ ]   |    30     | Substring with Concatenation of All Words      | Sliding window with careful counting. Each word has the same length. Maintain frequency counts of words in the current window, move in steps of `word_length`.                    |
|  [ ]   |    76     | Minimum Window Substring                       | Keep expanding the right pointer to include characters until meeting the requirement. Then contract from the left to find the minimal window that still satisfies the need.       |
|  [ ]   |    209    | Minimum Size Subarray Sum                      | Maintain a running sum with a sliding window. Expand right pointer to increase sum; once sum >= target, shrink from the left to try to get a smaller valid subarray.              |
|   ✅    |    121    |                       |              |
|  ✅   |    238    |                       |              |
|  [ ]   |    239    | Sliding Window Maximum                         | Use a deque to maintain indices of elements in descending order. The front of the deque is the current window's max. When sliding, remove elements out of range or smaller.       |
|  ✅   |    242    |                       |              |
|  [ ]   |    271    |                       |              |
|  ✅   |    347    |                       |              |
|  [ ]   |    438    | Find All Anagrams in a String                  | Sliding window of size `p.length()`. Maintain char frequency counts. When the window size exceeds `p.length()`, move the left pointer. Compare counts to know if it's an anagram. |
|  [ ]   |    567    | Permutation in String                          | Sliding window with frequency count of `s1`. Expand right pointer, update count. If the window size is `s1.length()`, check if counts match. Move left pointer accordingly.       |
|  [ ]   |    713    | Subarray Product Less Than K                   | Keep a running product. Expand right pointer, while product >= K, move left pointer to reduce the product. The count is related to the window size each time right expands.       |
|  [ ]   |   1004    | Max Consecutive Ones III                       | Sliding window. We can flip up to `k` zeroes. Expand right pointer, track how many zeroes are in the window. If zero count > k, shrink from the left until zero count ≤ k.        |
|  [ ]   |   1052    | Grumpy Bookstore Owner                         | Use a sliding window of size `X` to identify which segment to “use magic” on. Calculate the base satisfaction plus the extra gained by making grumpy owners happy in the window.  |
|  [ ]   |   1248    | Count Number of Nice Subarrays                 | Sliding window approach to track number of odd elements in the window. Use prefix sums or a two-pointer technique to find subarrays that contain exactly k odd numbers.           |

---
