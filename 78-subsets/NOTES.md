# we have to find all the possible subsets
# as the constraint is very small, we obiously have to use backtracking
# as it will not contain any duplicate item
res = set()
# an recursive function of our backtracking
def bt(i,subset):
# Adding the item in the res
res.add(tuple(subset))
# our bounding condition, we have reached the last item in the list
if i == len(nums):
return
# choosing the item
bt(i+1,subset + [nums[i]])
# without choosing the item
bt(i+1,subset)
# Calling the function
bt(0,[])
return res