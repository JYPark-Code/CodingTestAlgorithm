import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        int start = 0;
        int end = arr.length; // 잘라낼 범위 [start, end)
        for (int i = 0; i < query.length; i++) {
            int idx = query[i];
            if (i % 2 == 0) {
                // 짝수 → 뒷부분 버리기
                end = start + idx + 1;
            } else {
                // 홀수 → 앞부분 버리기
                start = start + idx;
            }
        }
        if (start >= end) {
            return new int[]{-1};
        }
        return Arrays.copyOfRange(arr, start, end);
    }
}