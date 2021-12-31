# 예외 처리 한 개 필요
# 2개 선택해서 비교하는 것 외에, 남은 나머지 것들에 대해서도 조건 처리를 해줘야 함

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