import java.util.*;
import java.util.stream.*;

class Solution {
    public List<Integer> solution(int[] arr) {
        
        List<Integer> answer = Arrays.stream(arr)
            .boxed()
            .collect(Collectors.toList());
        
        int power = 0;
        
        while(arr.length > Math.pow(2,power)){
            power += 1;
        }
        
        // System.out.print(power);
        
        answer.addAll(Collections.nCopies((int)Math.pow(2,power) - arr.length, 0));
        // System.out.print((int)Math.pow(2,power)+ " " +arr.length);
        return answer;
    }
}