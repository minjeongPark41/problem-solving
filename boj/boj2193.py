# Q. 2193
n = int(input())
dp = [(0, 0) for _ in range(n+1)]  # 끝이 0인 / 끝이 1인
dp[1] = (0, 1)
# dp[2] = (1, 0) 이건 아래 식으로 구할 수 있기에 안 넣어줘도 되고, 넣어주면 되려 out of index 오류 남. 만약 n=0 들어오면 2까지 안가기에 

if n >= 2:
    for i in range(2, n+1):
        dp[i] = (sum(dp[i-1]), dp[i-1][0])
    
print(sum(dp[n]))
