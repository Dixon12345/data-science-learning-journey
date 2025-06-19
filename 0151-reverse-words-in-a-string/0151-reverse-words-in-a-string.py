class Solution:
    def reverseWords(self, s: str) -> str:
        list = s.split()
        list.reverse()
        return " ".join(list)
        