# 예외 처리 한 개 필요

def solution(P):
    ans = []
    num = len(P)
    
    for i in range(1, num):
        word = P[0] + P[i]
        word2 = P[i] + P[0]
        if word == word[::-1] or word2 == word2[::-1]: 
            if P[0] != P[i]:
                ans.append(P[i])
                
    
    return ans

solution(["11","111","11","211"])