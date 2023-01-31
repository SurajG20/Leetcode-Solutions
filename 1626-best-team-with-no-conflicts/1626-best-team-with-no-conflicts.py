class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores) # length of scores for initialising dp array.... 
        print("n",n)
        
        dp = [0] * n # Dp to store score for step
        print("dp",dp)
        
        ans = 0 # Answer to return 
        print("ans",ans)
        
        players = [(ages[i], scores[i]) for i in range(n)] # Pair of ages and scores 
        print("players",players)
        
        players.sort(key = lambda x: x[0]) # Arranging the pair according to ages
        print("players",players)
        
        for i in range(n): # Iterating over the pair array
            print("i",i)
            
            dp[i] = players[i][1] # Storing the cuurent score in dp array
            print("dp",dp)
            
            for j in range(i): 
                print("j",j)
                # Then we check for previous score in dp array.
                # but add only when the current score the previous score 
                # because as ages are sorted, the score must be sorted too..
                if players[j][1] <= players[i][1]:
                    # Keep changing the value of dp item, according to condition
                    dp[i] = max(dp[i], dp[j] + players[i][1])
                    print("dp",dp)
            # Also keep updating the answer        
            ans = max(ans, dp[i])
            print("ans",ans)
        return ans
    
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        # We create a dp array of size `max(ages) + 1` ~ because the indexing start from 0
        dp = [0] * (1+max(ages))   
        
        # (Scores and ages) sorted by scores                                 
        score_age = sorted(zip(scores, ages))
          
        # We iterate for scores and ages    
        for score, age in score_age:            
            # store the current score + max(previous max dp element)                                   
            dp[age] = score + max(dp[:age+1])   
                                               
        return max(dp)                          
          
            #   Example: scores = [4,4,6,5]
            #              ages = [2,1,5,1]
            #         dp = [0, 0, 0, 0, 0] 
            #  score_age = [(4,1), (4,2), (5,1), (6,5)]
            #   score   age     dp
            #   –––––  –––––    ––––––––––––––––––
            #     4      1      [0, 4, 0, 0, 0, 0]
            #     4      2      [0, 4, 8, 0, 0, 0]
            #     5      1      [0, 9, 8, 0, 0, 0]
            #     6      5      [0, 9, 8, 0, 0,15] 
            #                                   |
            #                                 return 