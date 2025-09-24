# word_break.py
# Word Break Problem using Dynamic Programming

def wordBreak(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)  # Faster lookups
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always "breakable"

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to check further for this i

    return dp[n]


if __name__ == "__main__":
    # Example usage
    s = "leetcode"
    wordDict = ["leet", "code"]
    print("Input:", s)
    print("Dictionary:", wordDict)
    print("Can be segmented?", wordBreak(s, wordDict))  # Expected: True
