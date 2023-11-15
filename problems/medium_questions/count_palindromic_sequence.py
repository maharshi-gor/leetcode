class Solution:
    """
    Author: Maharshi Gor
    Date: 2023-11-15
    """
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        1930. Unique Length-3 Palindromic Subsequences

        Given a string s, return the number of unique palindromes of length
        three that are a subsequence of s.

        Note that even if there are multiple ways to obtain the same
        subsequence, it is still only counted once.

        A palindrome is a string that reads the same forwards and backwards.

        A subsequence of a string is a new string generated from the original
        string with some characters (can be none) deleted without changing the
        relative order of the remaining characters.

        Explanation
        -----------
        The problems asks us to find the number of palindromic sequences of size
        3. We can simply think it as how many unique characters are available
        between two same characters.

        As we think with this new point of view, how can we find all the possible
        unique characters, simple answer is just put whatever you find into set
        and count the set.

        We pickout two fathest same character pick the characters between put
        them in a set and count them.
        """
        char_array = list(s)
        spans = dict()

        for i, c in enumerate(char_array):
            if spans.get(c) is None:
                spans[c] = [i, i]
            else:
                spans[c][1] = i

        def find_unique_chars_between(char_list):
            return len(set(char_list))

        result = 0
        for span in spans.values():
            result += find_unique_chars_between(char_array[(span[0]+1):span[1]])

        return result