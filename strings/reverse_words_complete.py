# TIME : 0(N), SPACE : 0(1),

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()[::-1]
        return " ".join(l)
