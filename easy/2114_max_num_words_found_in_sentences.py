# 2114. Maximum Number of Words Found in Sentences
# Difficulty: Easy
# Topic: Array, String
# Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

# ----------------------------
# Problem:
# Given an array of sentences, return the maximum number of words
# found in any single sentence.
# ----------------------------

# Approach: Track Running Max
# - split each sentence into words using .split() (splits on whitespace)
# - count the words in each sentence, compare against the running max
# - update max_words whenever a bigger count is found
# Time: O(n * m) | Space: O(1), where n = number of sentences, m = avg sentence length


class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0

        for sentence in sentences:
            words = sentence.split()
            count = len(words)

            if count > max_words:
                max_words = count

        return max_words


# ----------------------------
# Test cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()

    sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    print(f"mostWordsFound = {sol.mostWordsFound(sentences)}")  # 6

    sentences = ["please wait", "continue to fight", "continue to win"]
    print(f"mostWordsFound = {sol.mostWordsFound(sentences)}")  # 3

    sentences = ["single"]
    print(f"mostWordsFound = {sol.mostWordsFound(sentences)}")  # 1