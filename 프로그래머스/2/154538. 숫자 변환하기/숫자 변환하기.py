from collections import deque
def solution(x, y, n):
    
    queue = deque([(x, 0)])
    visited = set()
    
    while queue:
    
        current, count = queue.popleft()
    
        if current == y:
            return count

        if current in visited or current > y:
            continue

        visited.add(current)

        if current * 2 <= y and current * 2 not in visited:
            queue.append((current * 2, count + 1))

        if current * 3 <= y and current * 3 not in visited:
            queue.append((current * 3, count + 1))

        if current + n <= y and current + n not in visited:
            queue.append((current + n, count + 1))
            
    return -1
