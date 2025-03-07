N = int(input())
numbers = list(map(int, input().split()))

stack = []
answer = [-1] * len(numbers)

for i in range(len(numbers) - 1, -1, -1):
    
    while stack and stack[-1] <= numbers[i]:
        stack.pop()
        
    if stack:
        answer[i] = stack[-1]
    
    stack.append(numbers[i])

print(" ".join(map(str, answer)))