from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, target, words)

def bfs(begin, target, words):
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        current_word, steps = queue.popleft()
        
        if current_word == target:
            return steps
        
        for word in words:
            if word not in visited and is_convertible(current_word, word):
                queue.append((word, steps + 1))
                visited.add(word)
        
    
    return 0
    


def is_convertible(l1, l2):
    
    count = 0
    
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            count += 1
        
        if count > 1:
            return False
        
    if count == 1:
        return True
    
    