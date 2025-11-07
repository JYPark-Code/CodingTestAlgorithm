import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        Arrays.fill(answer, -1);          // 부족분은 -1로 패딩
        Set<Integer> seen = new HashSet<>();
        int idx = 0;

        for (int x : arr) {
            if (!seen.contains(x)) {      // 처음 본 값만 채우기
                answer[idx++] = x;
                seen.add(x);
                if (idx == k) break;      // k개 채우면 종료
            }
        }
        return answer;
    }
}