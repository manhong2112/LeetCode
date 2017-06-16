class Solution {
public:
    int findComplement(int num) {
        int k, tmp = 0;
        do {
            k |= ((num & 1) == 0) << tmp++;
        } while(num >>= 1);
        return k;
    }
};