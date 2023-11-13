class Solution:
    """
    Author: Maharshi Gor
    Date: 2023-11-13
    """
    def sortVowels(self, s: str) -> str:
        """
        Given a 0-indexed string s, permute s to get a new string t such that:

        All consonants remain in their original places. More formally, if there
        is an index i with 0 <= i < s.length such that s[i] is a consonant, then
        t[i] = s[i].
        The vowels must be sorted in the nondecreasing order of their ASCII
        values. More formally, for pairs of indices i, j with
        0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must
        not have a higher ASCII value than t[j].

        Return the resulting string.

        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in
        lowercase or uppercase. Consonants comprise all letters that are not
        vowels.

        Explanation
        -----------

        We are creating a dictionary of vowels' counts, which we will increase
        when we see a sepcific vowel. We don't want to extract all the vowels and
        then sort them. That will work but, it will exceed time limits.

        Here, we will record a specific vowel and count them and replace them
        while iterating again.
        """

        vowel_count = dict({
            'A': 0,
            'E': 0,
            'I': 0,
            'O': 0,
            'U': 0,
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        })

        t = list(s)

        def is_vowel(c):
            return vowel_count.get(c) is not None

        for c in t:
            if is_vowel(c):
                vowel_count[c] += 1

        vowels = list(vowel_count.keys())
        current_vowel = 0
        for idx, c in enumerate(t):
            if is_vowel(c):
                while vowel_count[vowels[current_vowel]] <= 0:
                    current_vowel += 1
                else:
                    vowel_count[vowels[current_vowel]] -= 1

                t[idx] = vowels[current_vowel]

        return ''.join(t)
