def solution(numbers, target):
    count = [0]  # 리스트로 선언하면 내부 함수에서 참조/수정 가능

    def dfs(index, total):
        if index == len(numbers):
            if total == target:
                count[0] += 1
            return
        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])

    dfs(0, 0)
    return count[0]