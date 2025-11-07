import java.util.*;

class Solution {
    public int solution(String[] order) {
        int answer = 0;
        Map<String, Integer> menu = new HashMap<>();
        
        menu.put("ame", 4500);
        menu.put("caf", 5000);
        menu.put("any", 4500);
        
        for(String drink : order){
            if (!menu.containsKey(drink.substring(0,3))){
                answer += menu.get(drink.substring(3,6));
            } else {
                answer += menu.get(drink.substring(0,3));
            }
        }
        
        return answer;
    }
}