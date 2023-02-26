In 1st try i used substring and checked for each substing starting from 0 to i+1 weather it is divisble by m or not but it was giving TLE during the contest.
​
we can keep track of modulo .
​
if we take modulo of a number with m then the size of the number will get reduced and remaider will remain,
and again checking if(remainder%m == 0) will check if number is divisible by m or not;
​
num = (num*10 + word[i]-'0')%m;
![](https://assets.leetcode.com/users/images/2242522c-680f-43a3-a506-e42b766ada53_1677384485.4976823.jpeg)