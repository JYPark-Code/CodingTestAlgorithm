import java.util.*;

class Solution {
    public int solution(int n, int w, int num) {
        List<Integer> boxes = new ArrayList<>();

        int base = n / w;     // 기본적으로 각 열에 몇 개씩 들어가는가
        int mod = n % w;      // 나머지 상자 수

        // 기본 높이 배분
        for (int i = 0; i < w; i++) {
            boxes.add(base);
        }

        // 분배 방향: base(=줄 수)의 홀짝에 따라 오른쪽 또는 왼쪽부터 채움
        if (base % 2 == 0) {
            // 짝수 → 왼쪽부터
            for (int i = 0; i < mod; i++) {
                boxes.set(i, boxes.get(i) + 1);
            }
        } else {
            // 홀수 → 오른쪽부터
            for (int i = w - 1; i >= w - mod; i--) {
                boxes.set(i, boxes.get(i) + 1);
            }
        }

        // num 좌표 계산 (0-based)
        int numIndex = num - 1;
        int y = numIndex / w;
        int x = numIndex % w;

        // 홀수 줄이면 반전
        if (y % 2 == 1) {
            x = w - 1 - x;
        }

        // 정답: 해당 열 높이 - y
        int answer = boxes.get(x) - y;
        return answer;
    }
}
