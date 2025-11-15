import java.util.*;

class Solution {
    public String solution(String s) {
        
        List<Integer> numList = new ArrayList<>();
        
        for (String num : s.split(" ")){
            numList.add(Integer.parseInt(num));
        }
        
        int minNum = Collections.min(numList);
        int maxNum = Collections.max(numList);
        
        return minNum + " " + maxNum;
    }
}