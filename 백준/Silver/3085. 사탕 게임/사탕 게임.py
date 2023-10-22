# 인접한 두칸 바꿔서 행 또는 열 최대치 리턴
# N X N
# N = 3 ~ 50
# 색깔은 C,P,Z,Y

N = int(input())

graph = []
answer = 0

for _ in range(N):
    graph.append(list(input()))

# print(graph)

# 구상한 방법 행 체크 , 열 체크 , 갯수 세기

def count_col_row(graph):
    # element = ["C", "P", "Z", "Y"]
    xMax = 0
    x_count = 1
    yMax = 0
    y_count = 1

    for i in range(N):
        x_count = 1
        y_count = 1
        for j in range(N - 1):
            if graph[i][j] == graph[i][j+1]:
                x_count += 1
                xMax = max(xMax, x_count)
            elif graph[i][j] != graph[i][j+1]:
                x_count = 1

            if graph[j][i] == graph[j+1][i]:
                y_count += 1
                yMax = max(yMax, y_count)
            elif graph[j][i] != graph[j+1][i]:
                y_count = 1

            max_num = max(xMax, yMax)

    return max_num


# print(count_col_row(graph))

# 스왑하기
#  행 체크
for i in range(N):
    for j in range(N - 1):
        if graph[i][j] != graph[i][j+1]:
            # 스왑하고
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            answer = max(answer, count_col_row(graph))
            # print(i, j, i, j + 1, graph, answer)
            # 다시 원복
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            # print(graph)

            if graph[j][i] != graph[j + 1][i]:
                graph[j][i], graph[j + 1][i] = graph[j + 1][i], graph[j][i]
                answer = max(answer, count_col_row(graph))
                # print(j, i, j + 1, i, graph, answer)
                graph[j][i], graph[j + 1][i] = graph[j + 1][i], graph[j][i]

        elif graph[j][i] != graph[j+1][i]:
            graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]
            answer = max(answer, count_col_row(graph))
            # print(j, i, j + 1, i, graph, answer)
            graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]

print(answer)