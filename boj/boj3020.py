# 개똥벌레

# split은 기본값이 공백이라 그냥 .split() 해줘도 됨
n, h = map(int, input().split(' '))

# 석순, 종유석 '길이' 넣어주기
length = [] #[1, 5, 3, 3, 5, 1]
for i in range(n):
  length.append(int(input()))

answer = [0] * (h + 1)
top = [0] * (h + 1) #[0, 0, 0 ....] #석순 
bottom = [0] * (h + 1) #종유석 

count = 0
for data in length:
  if count % 2 == 0: #0, 2, 4,... 번째. 즉, 석순
    count += 1
    top[data] += 1 #길이를 인덱스 삼아, +=1 로 세워주는거
  else: #종유석 
    count += 1
    bottom[h-data+1] += 1

for i in range(h - 1, 0, -1):
  top[i] += top[i + 1]

# 그낭 h부터 하면 0~h-1이니 헷갈리니
for i in range(1, h + 1):
  bottom[i] += bottom[i-1]

for i in range(1, h + 1):
  answer[i] = top[i] + bottom[i]

answer = answer[1:]
print(min(answer), answer.count(min(answer)))