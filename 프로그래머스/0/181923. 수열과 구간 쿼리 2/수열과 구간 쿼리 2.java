import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr, int[][] queries) {
        List<Integer> answer = new ArrayList<>();
        
        for (int[] query : queries){
            int s = query[0];
            int e = query[1];
            int k = query[2];
            
            List<Integer> list = new ArrayList<>();
            
            for(int i = s; i <= e; i++) {
                if(arr[i] > k){
                    list.add(arr[i]);
                }
            }
            
            if(list.isEmpty()){
                answer.add(-1);
            } else {
                answer.add(Collections.min(list));
            }
                
        }
        
        return answer;
    }
}