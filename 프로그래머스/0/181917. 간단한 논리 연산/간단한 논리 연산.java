import java.util.*;

class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean first = true;
        boolean second = true;
        boolean answer = false;
        
        if (x1 == false && x2 == false){
            first = false;
        }
        
        if (x3 == false && x4 == false){
            second = false;
        }
        
        if (first && second){
            answer = true;
        }
        
        return answer;
    }
}