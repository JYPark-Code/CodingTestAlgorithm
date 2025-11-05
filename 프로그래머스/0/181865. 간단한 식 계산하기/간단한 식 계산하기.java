import java.util.*;
class Solution {
    public int solution(String binomial) {
        List<String> splitList = new ArrayList<>(Arrays.asList(binomial.split(" ")));
        // System.out.println(splitList);
        int a = Integer.parseInt(splitList.get(0));
        int b = Integer.parseInt(splitList.get(2));
        String op = splitList.get(1);
        
        if (op.equals("+")){
            return a + b;
        } else if(op.equals("-")){
            return a - b;
        } else {
            return a * b;
        }
    }
}