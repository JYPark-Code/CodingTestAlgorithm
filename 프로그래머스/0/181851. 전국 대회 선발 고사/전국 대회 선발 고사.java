import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int n = rank.length;

        // 사람 인덱스 배열 [0..n-1]
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;

        // 등수 기준 오름차순 정렬
        Arrays.sort(idx, Comparator.comparingInt(i -> rank[i]));

        // 참석 가능한 상위 3명의 "사람 인덱스" 추출
        List<Integer> picked = new ArrayList<>(3);
        for (int i = 0; i < n && picked.size() < 3; i++) {
            int person = idx[i];
            if (attendance[person]) picked.add(person);
        }

        // 문제식: 10000*a + 100*b + c  (a,b,c는 사람 인덱스)
        return 10000 * picked.get(0) + 100 * picked.get(1) + picked.get(2);
    }
}