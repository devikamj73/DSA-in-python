class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        solution = float('inf')
        gap = float('inf')

        for num in nums:
            if abs(num) < gap:
                gap = abs(num)
                solution = num
            elif abs(num) == gap:
                solution = max(solution, num)
        
        return solution