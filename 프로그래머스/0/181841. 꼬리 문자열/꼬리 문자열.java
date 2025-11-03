class Solution {
    public String solution(String[] str_list, String ex) {
        String answer = "";

        for (String s : str_list) {
            if (s.contains(ex)) { // ✅ 포함되어 있으면 건너뛴다
                continue;
            } else {
                answer += s;     // 포함되지 않으면 이어 붙인다
            }
        }

        return answer;
    }
}
