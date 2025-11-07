import java.util.*;
// 문제를 다시 읽을 것
// 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더합니다.
class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        
        int[] answer = Arrays.copyOf(arr, arr.length);
        
        for(int[] query : queries){
            int s = query[0];
            int e = query[1];
            int k = query[2];
            
            for(int i = s; i <= e; i++){
                if (i % k == 0){
                    answer[i] += 1;
                }
                // System.out.println(Arrays.toString(answer));
            }
            
        }

        return answer;
    }
}