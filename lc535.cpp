class Solution {
    
public:
    vector<string> url;
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        int x = url.size();
        url.push_back(longUrl);
        return std::to_string(x);
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return url[std::stoi( shortUrl )];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));