import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        
        List<Integer> answer = new ArrayList<>();
        boolean flag = false;
        
        for(int i = 0 ; i < arr.length; i++){
            if (arr[i] == 2){
                flag = true;
                answer.add(i);
            }
        }
        
        if (!flag){
            return new int[]{-1};
        }
        
        
        return Arrays.copyOfRange(arr, Collections.min(answer), Collections.max(answer) + 1);
        
    }
}