n = int(input())
data = 1
stack = []
result = []

for i in range(1, n+1):
    number = int(input())
    while data <= number:
        stack.append(data)
        data +=1
        result.append('+') # 문제에서 출력해줘야 하는 답의 형식 
    if stack[-1] == number:
        stack.pop(data)
        result.append('-')
    else:
        print('No')
        exit(0) #종료
        
print('\n'.join(result))
    
        