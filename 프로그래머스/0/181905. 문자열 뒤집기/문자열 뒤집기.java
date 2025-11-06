class Solution {
    public String solution(String my_string, int s, int e) {
        String reversed = new StringBuilder(my_string.substring(s, e + 1)).reverse().toString();
        String answer = my_string.substring(0, s) + reversed + my_string.substring(e + 1); 
        return answer;
    }
}