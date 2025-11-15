import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        // Stack 과 Queue 둘다 Deque를 사용한다.
        Deque<Character> stack = new ArrayDeque<>();
        
        for(char c : s.toCharArray()){
            if(stack.isEmpty()){
                if (c == ')'){
                    return false;
                }
            } 
             
            if(c == '('){
                stack.push(c);
            } else {
                stack.pop();
            }
            
        }
        
        if(stack.isEmpty()){
            return true;
        }

        return false;
    }
}