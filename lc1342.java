class Solution {
   public int numberOfSteps(int num) {
      int count = 0;
      int n = num;
      do {
         count += (n & 1) + 1;
      } while ((n >>= 1) != 0);
      return count - 1;
   }
}
