# Word Break Problem (Dynamic Programming)

This repository contains a Python implementation of the classic **Word Break Problem**.

## Problem Statement
Given a string `s` and a dictionary of strings `wordDict`, return `True` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

- The same word in the dictionary may be reused multiple times in the segmentation.
- All strings consist of lowercase English letters only.

### Example
**Input:**
```
s = "leetcode"
wordDict = ["leet","code"]
```

**Output:**
```
True
```
**Explanation:**  
`"leetcode"` can be segmented as `"leet code"`.

---

## Approach
This problem is solved using **Dynamic Programming (DP)**.

- Use a DP array `dp` of size `n+1` where `dp[i]` is `True` if the substring `s[0:i]` can be segmented into dictionary words.
- Initialize `dp[0] = True` (empty string is always valid).
- For each index `i`, check all possible partitions `s[j:i]` where `0 ≤ j < i`.  
  If `dp[j]` is `True` and `s[j:i]` is in `wordDict`, then set `dp[i] = True`.

Finally, return `dp[n]`.

---

## Complexity
- **Time Complexity:** O(n²)  
- **Space Complexity:** O(n)  

---

## Files
- `word_break.py` → Contains the Python implementation and example usage.

---

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/word-break-dp.git
   cd word-break-dp
   ```

2. Run the program:
   ```bash
   python word_break.py
   ```

Expected output:
```
Input: leetcode
Dictionary: ['leet', 'code']
Can be segmented? True
```

---

## License
This project is open-source and available under the MIT License.
