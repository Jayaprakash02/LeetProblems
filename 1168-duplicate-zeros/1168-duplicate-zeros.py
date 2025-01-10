class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = n - 1
        while i >= 0:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
            i -= 1
        