class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        stringstream res, sa(a), sb(b);
        char abc;
        int na, nb, nc, nd;
        sa >> na >> abc >> nb;
        sb >> nc >> abc >> nd;
        res << (na * nc - nb * nd) << "+" << (na * nd  + nb * nc) << "i";
        return res.str();
    }
};