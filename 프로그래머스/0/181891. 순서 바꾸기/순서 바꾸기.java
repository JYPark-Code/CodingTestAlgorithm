import java.util.Arrays;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] num_list, int n) {
        
        int [] front = Arrays.copyOfRange(num_list, n, num_list.length);
        int [] back = Arrays.copyOfRange(num_list, 0 , n);  
        
        int[] answer = IntStream.concat(IntStream.of(front), IntStream.of(back))
                                .toArray();
        return answer;
        
    }
}