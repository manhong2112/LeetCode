class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        std::sort (nums.begin(), nums.end());
        int k = 0;
        for(int i = 0;i<nums.size();i+=2) {
            k += nums[i];
        }
        return k;
    }
};