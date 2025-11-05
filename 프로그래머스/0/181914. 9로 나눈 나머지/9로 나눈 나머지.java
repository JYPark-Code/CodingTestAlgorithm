import java.math.BigInteger;

class Solution {
    public int solution(String number) {
        BigInteger bigNum = new BigInteger(number);
        return bigNum.mod(BigInteger.valueOf(9)).intValue(); // 9로 나눈 나머지
    }
}