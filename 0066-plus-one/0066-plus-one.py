class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''.join(map(str,digits))
        b = list(str(int(a)+1))
        c = list(map(int,b))
        return c