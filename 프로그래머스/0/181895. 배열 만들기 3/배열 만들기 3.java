import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr, int[][] intervals) {
        List<Integer> answer = new ArrayList<>();
        
        for(int[] interval : intervals){
            int a = interval[0];
            int b = interval[1];
            
            // arr은 배열이라 substring이 아니라 slice 처리를 직접 해야 함
            for (int i = a; i <= b; i++) {
                answer.add(arr[i]);
            }
        }
        
        return answer;
    }
}