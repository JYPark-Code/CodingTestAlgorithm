import sys
input = sys.stdin.readline

T = int(input().strip())

ranking_board = []

for _ in range(T):
    applicant = int(input().strip())
    ranking_board = []
    for _ in range(applicant):
        paper_rank, interview_rank = map(int, input().split())
        ranking_board.append((paper_rank, interview_rank))

    ranking_board.sort()
    # print(ranking_board)
    
    count = 1
    compare_paper, compare_interview = ranking_board[0][0], ranking_board[0][1]

    for paper, interview in ranking_board[1:]:
        if compare_paper > paper or compare_interview > interview:
            count += 1
            compare_paper = paper
            compare_interview = interview

    print(count)