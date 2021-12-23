import sys

string_a = ' ' + sys.stdin.readline().rstrip() # 아래 1부터 시작한 이유 (index 0인 부분, 즉 처음을 ' ' 빈 공백으로 준 것)
string_b = ' ' + sys.stdin.readline().rstrip()
dp = [[0] * len(string_b) for _ in range(len(string_a))]

for i in range(1, len(string_a)):
    for j in range(1, len(string_b)):
        if string_a[i] == string_b[j]: # 같은거 만났을 때는 LCS 조건에 부합하니까 +1
            dp[i][j] = dp[i - 1][j - 1] + 1 
        else: # 만약에 다르다면, 그 이전에 구한(그래서 dp 개념) 최대값을 끌고 와줘야 함
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 
            
print(dp[-1][-1])