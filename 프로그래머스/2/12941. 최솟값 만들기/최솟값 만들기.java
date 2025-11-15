import java.util.*;

class Solution
{
    public int solution(int[] A, int[] B) {
        Arrays.sort(A);         // 오름차순
        Arrays.sort(B);         // 오름차순

        int answer = 0;
        int n = A.length;

        for (int i = 0; i < n; i++) {
            answer += A[i] * B[n - 1 - i];   // 작은 A * 큰 B
        }

        return answer;
    }
}