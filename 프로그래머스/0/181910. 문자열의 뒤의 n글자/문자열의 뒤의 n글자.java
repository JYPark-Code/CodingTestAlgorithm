class Solution {
    public String solution(String my_string, int n) {
         // 문자열의 길이를 구한다
        int length = my_string.length();

        // substring(시작 인덱스) 는 끝까지 잘라줌
        // 뒤에서 n글자를 얻으려면 length - n 위치부터 잘라야 함
        return my_string.substring(length - n);
    }
}