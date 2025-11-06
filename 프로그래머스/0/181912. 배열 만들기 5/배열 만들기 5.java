import java.util.*;

class Solution {
    public List<Integer> solution(String[] intStrs, int k, int s, int l) {
        List<Integer> answer = new ArrayList<>();
        
        for (String numStr : intStrs){
            String sub_st = numStr.substring(s, s + l);
            int sub_int = Integer.parseInt(sub_st);
            if (sub_int > k){
                answer.add(sub_int);
            }
            
        }
        
        
        return answer;
        
        
        
        
    }
}