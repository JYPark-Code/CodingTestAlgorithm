class Solution {
    public String solution(String myString) {
        String lowercase = myString.toLowerCase(); 
        String answer = lowercase.replace("a","A");
        return answer;
    }
}