import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = Arrays.copyOf(arr, arr.length);
        
        for (int[] query : queries){
            
            int a = query[0];
            int b = query[1];
            
            for (int i = a; i <= b; i++){
                answer[i] += 1;
            }
        }
        
        return answer;
    }
}