object Solution {
    def smallerNumbersThanCurrent(nums: Array[Int]): Array[Int] = {
        val res = new Array[Int](nums.length);
        var n = 0;
        for(i <- nums) {
            for(j <- nums) {
                if(j < i) {
                    res(n) += 1;
                }
            }
            n += 1;
        }
        res
    }
}
