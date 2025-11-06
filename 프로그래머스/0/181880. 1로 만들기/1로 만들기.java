class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        for (int num: num_list){
            int power = 0;
            while( num >= Math.pow(2, power)){
                power += 1;
                // System.out.println(num + " power: " + power);
            }
            answer += power - 1;
        }
        return answer;
        
    }
}