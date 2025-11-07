import java.util.*;

class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];

        // 오른쪽, 아래, 왼쪽, 위 순서
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};

        int x = 0, y = 0, dir = 0; // 시작 위치(0,0), 방향=오른쪽

        for (int i = 1; i <= n * n; i++) {
            answer[x][y] = i;

            // 다음 칸 예상
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            // 경계 밖이거나 이미 채워졌다면 방향 전환
            if (nx < 0 || ny < 0 || nx >= n || ny >= n || answer[nx][ny] != 0) {
                dir = (dir + 1) % 4; // 방향 전환
                nx = x + dx[dir];
                ny = y + dy[dir];
            }

            // 이동
            x = nx;
            y = ny;
        }

        return answer;
    }
}
