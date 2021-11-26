n = int(input())
data = 1
stack = []
result = []

for i in range(1, n+1):
    number = int(input())
    while data <= number:
        stack.append(data)
        data +=1
        result.append('+')
    if stack[-1] == number:
        stack.pop(data)
        result.append('-')
    else:
        print('No')
        exit(0)
        
print('\n'.join(result))
    
        