import java.util.*;

class Solution {
    public int solution(int[] num_list) {
        List<Integer> odd = new ArrayList<>();
        List<Integer> even = new ArrayList<>();
        
        for (int num : num_list){
            if (num % 2 == 0){
                even.add(num);
                continue;
            }
            odd.add(num);
        }
        
        // System.out.println(odd);
        // System.out.println(even);
        
        int odd_length = odd.size() - 1;
        int even_length = even.size() - 1;
        
        int odd_total = 0;
        int even_total = 0;
        
        for (int num : odd){
            odd_total = odd_total +  (num *  ((int)Math.pow(10, odd_length)));
            odd_length -= 1;
                                     
        }
        
        for (int num : even){
            even_total = even_total +  (num * ((int)Math.pow(10, even_length)));
            even_length -= 1;
                                     
        }
        
        return odd_total + even_total;
    }
}