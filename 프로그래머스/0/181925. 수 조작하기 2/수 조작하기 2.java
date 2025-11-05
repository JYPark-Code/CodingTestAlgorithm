import java.util.*;

class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        Map<Integer, String> wasd = new HashMap<>();
        
        wasd.put(1, "w");
        wasd.put(-1, "s");
        wasd.put(10, "d");
        wasd.put(-10, "a");
        
        for (int i = 1; i < numLog.length; i++){
            int diff = numLog[i] - numLog[i - 1];
            answer += wasd.get(diff);
        }
        
        return answer;
    }
}