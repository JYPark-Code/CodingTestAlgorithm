import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] cnt = new int[7];
        int[] nums = {a, b, c, d};
        for (int x : nums) cnt[x]++;

        int maxCnt = 0, maxVal = 0;
        for (int v = 1; v <= 6; v++) {
            if (cnt[v] > maxCnt) {
                maxCnt = cnt[v];
                maxVal = v;
            }
        }

        if (maxCnt == 4) {
            // 네 개 모두 같은 경우
            return 1111 * maxVal;
        } else if (maxCnt == 3) {
            // 세 개 같은 경우: (10*p + q)^2
            int p = maxVal, q = 0;
            for (int v = 1; v <= 6; v++) if (cnt[v] == 1) q = v;
            int t = 10 * p + q;
            return t * t;
        } else if (maxCnt == 2) {
            // 2,2 또는 2,1,1
            List<Integer> twos = new ArrayList<>();
            List<Integer> ones = new ArrayList<>();
            for (int v = 1; v <= 6; v++) {
                if (cnt[v] == 2) twos.add(v);
                else if (cnt[v] == 1) ones.add(v);
            }
            if (twos.size() == 2) {
                int p = twos.get(0), q = twos.get(1);
                return (p + q) * Math.abs(p - q);
            } else {
                int r = ones.get(0), s = ones.get(1);
                return r * s;
            }
        } else {
            // 모두 다름: 최소값
            int m = nums[0];
            for (int x : nums) m = Math.min(m, x);
            return m;
        }
    }
}
