N = int(input())

start = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
question = "\"재귀함수가 뭔가요?\""
answer_b4_condition_1 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
answer_b4_condition_2 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
answer_b4_condition_3 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
answer_af_condition = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
ending = "라고 답변하였지."


def answer(n, depth):
    """
    if 바닥 :
        답변 출력
    else:
        이야기 3줄 출력
        answer(depth + 1)

    마지막에 "라고 답변하였지." 출력
    """

    rec = "____" * depth
    print(rec + question)

    if n == 0:
        print(rec + answer_af_condition)
    else:
        print(rec + answer_b4_condition_1)
        print(rec + answer_b4_condition_2)
        print(rec + answer_b4_condition_3)
        answer(n-1, depth+1)

    print(rec + ending)


print(start)
answer(N , 0)