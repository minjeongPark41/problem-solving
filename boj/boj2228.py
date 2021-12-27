n,m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

# n * m+1 (음의 무한대 - 초기값을 가장 작은 값으로 넣어준 것. 비교해서 업데이트 시켜주기 위해)
# 초기값을 0으로 설정해주면 최대값이 음수가 될 수 있기 때문에 답이 올바르게 나오지 않게된다.

dp1 = [[-float('inf') for _ in range(m + 1)] for _ in range(n)] 
dp2 = [[-float('inf') for _ in range(m + 1)] for _ in range(n)]

dp1[0][0] = 0
dp2[0][1] = arr[0]

for i in range(1, n):
    dp1[i][0] = 0
    dp2[i][0] = -float('inf')
    for j in range(1, min(m, (i + 2) // 2) + 1):
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j])
        dp2[i][j] = max(dp1[i-1][j-1] + arr[i], dp2[i-1][j] + arr[i])


print(max(dp1[n-1][m], dp2[n-1][m]))


