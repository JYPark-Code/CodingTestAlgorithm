import java.util.*;

class Solution {
    public List<String> solution(String[] strArr) {
        
        List<String> answer = new ArrayList<>();
        
        for(String s : strArr) {
            if (s.contains("ad")){
                continue;
            }
            answer.add(s);
        }

        return answer;
    }
}