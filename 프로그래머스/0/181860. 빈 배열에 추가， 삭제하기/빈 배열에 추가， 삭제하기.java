import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr, boolean[] flag) {
        List<Integer> answer = new ArrayList<>();
        
        for(int i = 0; i < flag.length; i++){
            if (flag[i]){
                answer.addAll(Collections.nCopies(arr[i]*2, arr[i]));
            } else {
                answer.subList(answer.size() - arr[i] , answer.size()).clear();
            }
        }
        
        
        return answer;
    }
}