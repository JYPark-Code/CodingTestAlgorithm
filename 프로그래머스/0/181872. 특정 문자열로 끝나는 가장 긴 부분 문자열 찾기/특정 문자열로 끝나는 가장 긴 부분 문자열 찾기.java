class Solution {
    public String solution(String myString, String pat) {
        int end_num = 0;
        for(int i = myString.length(); i >= 0; i--){
            if (pat.equals(myString.substring(i - pat.length(), i))){
                return myString.substring(0, i);
            }
        }
        return "";
    }
}