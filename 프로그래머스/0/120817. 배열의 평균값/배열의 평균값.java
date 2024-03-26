class Solution {
    public double solution(int[] numbers) {
        int sum = 0, cnt = 0;
        for (int i : numbers) {
            sum += i;
            cnt++;
        }
        
        double answer = (double) sum / cnt;
        return answer;
    }
}