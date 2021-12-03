n = int(input())
array = list(map(int, input().split()))

dp = [1] * n # [1, 1, 1, 1, 1, 1] 
for i in range (1, n): # 1 ~ n-1
    for j in range (0, i): # 0 ~ n-2 (결국, 0 ~ n-1까지 다 비교하게 되는 것)
        if array[j] < array[i]: 
            dp[i] = max(dp[i], dp[j] + 1) # 여기가 핵심! 
            
print(max(dp)) # dp를 다 1로 채워줬었고, max(dp) 하면 '내 로직'에 들어맞는 값이 나오는 것
        
"""
[10, 20, 10, 30, 20, 50]

[1, 2, 1, 1, 1, 1] i는 1 j는 0
[1, 2, 1, 2, 1, 1] i는 3 j는 0
[1, 2, 1, 3, 1, 1] i는 3 j는 1
[1, 2, 1, 3, 1, 1] i는 3 j는 2
[1, 2, 1, 3, 2, 1] i는 4 j는 0
[1, 2, 1, 3, 2, 1] i는 4 j는 2
[1, 2, 1, 3, 2, 2] i는 5 j는 0
[1, 2, 1, 3, 2, 3] i는 5 j는 1
[1, 2, 1, 3, 2, 3] i는 5 j는 2
[1, 2, 1, 3, 2, 4] i는 5 j는 3
[1, 2, 1, 3, 2, 4] i는 5 j는 4
"""
 