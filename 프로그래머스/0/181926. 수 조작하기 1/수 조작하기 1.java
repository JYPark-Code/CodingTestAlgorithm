import java.util.*;

class Solution {
    public int solution(int n, String control) {
        Map<String, Integer> dict = new HashMap<>();
        
        dict.put("w", 1);
        dict.put("s", -1);
        dict.put("d", 10);
        dict.put("a", -10);
        
        for (char c : control.toCharArray()){
            n += dict.get(String.valueOf(c));    
        }

        return n;
    }
}