class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)
        minimum = min(salary)
        maximum = max(salary)
        n = len(salary)
        return (total - minimum - maximum)/(n-2)