class Solution {
public:
    int hammingDistance(int x, int y) {
        long k = x ^ y;
        int i = 0;
        do {
            i += k & 1;
        } while(k >>= 1);
        return i;
    }
};