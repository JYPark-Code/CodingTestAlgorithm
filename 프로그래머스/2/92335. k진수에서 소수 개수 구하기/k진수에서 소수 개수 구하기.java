import java.util.*;
class Solution {
    public int solution(int n, int k) {
        
        int answer = 0;
        
        String converted_num = Integer.toString(n,k);
        // System.out.println(Integer.toString(n,k));
        String[] parts = converted_num.split("0");
        
        List<Long> numbers = new ArrayList<>();
        
        for (String p : parts) {
            if(!p.equals("") && !p.equals("1")){
                numbers.add(Long.parseLong(p));
            }
        }
        
        for (long num : numbers){
            if(isPrime(num)){
                answer += 1;
            }
        }

        return answer;
    }
    
    public boolean isPrime(long n){
        if (n <= 1) return false;
        for(int i = 2; i <= Math.sqrt(n); i++){
            if (n % i == 0) return false;
        }
        return true;
    }
}