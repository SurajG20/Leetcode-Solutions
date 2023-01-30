class Solution:
    def tribonacci(self, n: int) -> int:
        # Simple memozization using hashmap
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        # Hash_Map
        hash_map = [0] * ( n + 1)
        
        hash_map[0] = 0
        hash_map[1] = 1
        hash_map[2] = 1
        
        for i in range(3,n+1):
            hash_map[i] = hash_map[i-1] + hash_map[i-2] + hash_map[i-3]
            
        return hash_map[n]
        
        
            
        