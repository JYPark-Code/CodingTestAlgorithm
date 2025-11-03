import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int last = num_list[num_list.length - 1];
        int b4last = num_list[num_list.length - 2];
        int newValue = 0;
        
        if (last > b4last) {
            newValue = last - b4last;
        }
        else {
            newValue = last * 2;
        }
        
        int[] answer = Arrays.copyOf(num_list, num_list.length + 1);
        answer[answer.length - 1] = newValue;
        return answer;
    }
}