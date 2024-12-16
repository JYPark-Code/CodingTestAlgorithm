class Solution {
    public int solution(int[] numbers, int n) {
        
        int size = numbers.length;
        int sum = 0;
        
        for(int i = 0; i < size; i++){
            sum += numbers[i];
            if(sum > n){
                return sum;
            }
        }
        return 0;
    }
}