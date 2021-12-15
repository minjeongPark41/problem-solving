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
    top[data] += 1 #길이를 인덱스 삼아, 개수를 세어준다. 예를 들어서 길이가 1인게 2개가 있으면 -> top[]의 index 1 자리에는 2가 자리하겠지.
  else: #종유석 
    count += 1
    bottom[h-data+1] += 1 # h-data까지만 하면 걸리는 부분이 없으니 +1

for i in range(h - 1, 0, -1): #h-1부터 -1까지 -1씩 작아지는거 (지금 h가 7이면, 6부터 -1까지)
  top[i] += top[i + 1] #top[6] += top[7], top[5] += top[6]... 이런식으로 가는건데 위에서 인덱스 삼아서 개수 세어줬던 걸 뒤에서부터 쭉 누적합 해주는 것

# 그낭 h부터 하면 0~h-1이니 헷갈리니
for i in range(1, h + 1):
  bottom[i] += bottom[i-1] 

for i in range(1, h + 1):
  answer[i] = top[i] + bottom[i]

answer = answer[1:] #슬라이싱. 시작 index부터 끝까지
print(min(answer), answer.count(min(answer)))