class Solution {
    public int solution(int[] num_list) {
        
        int sum_total = 0;
        int mult_total = 1;
        
        for (int num : num_list){
            sum_total += num;
            mult_total *= num;
        }
        
        sum_total *= sum_total;
        
        if(mult_total < sum_total){
            return 1;
        }
        return 0;
    }
}