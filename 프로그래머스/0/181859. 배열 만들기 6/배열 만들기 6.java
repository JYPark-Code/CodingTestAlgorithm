import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        
        for(int i = 0; i < arr.length; i++){
            if (answer.isEmpty()){
                answer.add(arr[i]);
            } else {
                int last = answer.get(answer.size() - 1);
                if(last == arr[i]) {
                    answer.remove(answer.size() - 1);
                } else {
                    answer.add(arr[i]);
                }
            }   
        }
        
        if(answer.isEmpty()){
            return new ArrayList<>(Arrays.asList(-1));
        }
        
        return answer;
    }
}