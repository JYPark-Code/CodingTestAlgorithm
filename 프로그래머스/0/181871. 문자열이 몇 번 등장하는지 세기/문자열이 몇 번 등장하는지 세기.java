class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        for(int i = 0; i <= myString.length() - pat.length(); i++){
            if(myString.charAt(i) == pat.charAt(0)){
                if(myString.substring(i, i + pat.length()).equals(pat)){
                    answer += 1;
                }
            }
        }
        
        return answer;
    }
}