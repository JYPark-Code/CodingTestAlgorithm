import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> list = new ArrayList<>();

        for (int x = l; x <= r; x++) {
            if (isOnlyZeroOrFive(x)) {
                list.add(x);
            }
        }

        if (list.isEmpty()) return new int[]{-1};
        return list.stream().mapToInt(Integer::intValue).toArray();
    }

    private boolean isOnlyZeroOrFive(int x) {
        if (x == 0) return true; // 0은 자릿수가 0만 있으므로 허용
        while (x > 0) {
            int d = x % 10;
            if (d != 0 && d != 5) return false;
            x /= 10;
        }
        return true;
    }
}