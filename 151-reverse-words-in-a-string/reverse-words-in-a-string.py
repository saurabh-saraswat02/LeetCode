class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()

        reverse_word = words[::-1]

        reverse_str = ' '.join(reverse_word)


        return reverse_str
        