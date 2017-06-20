class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s), res;
        string buff;
        
        while (getline(ss, buff,' ')) {
            reverse(buff.begin(), buff.end());
            res << buff << " ";
        }
        return res.str().substr(0, s.size());
    }
};