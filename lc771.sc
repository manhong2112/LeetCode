object Solution {
    def numJewelsInStones(J: String, S: String): Int = {
        var n = 0
        for(c <- S) {
            if(J contains c) {
                n += 1
            }
        }
        n
    }
}
