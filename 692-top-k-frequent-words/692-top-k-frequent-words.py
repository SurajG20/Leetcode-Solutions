class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = defaultdict(int)
        
        for w in words:
            hashmap[w] += 1
          
        temp = []
        for key,val in hashmap.items():
            temp.append((-val,key))
            
        
        heapq.heapify(temp)
        
        print(temp)
        
        res = []
        while k:
            x,y = heapq.heappop(temp)
            res.append(y)
            k -= 1
            
        return res
            
            
            