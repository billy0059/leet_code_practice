class Solution {
public:
    bool isPalindrome(string s) {
        int l=0, r=s.size()-1;
        while (l<r){
            if (!(s[l] >= '0' && s[l] <= '9') && !(tolower(s[l]) >= 'a' && tolower(s[l])<='z')){
                l++;
                continue;
            }
            else if (!(s[r] >= '0' && s[r] <= '9') && !(tolower(s[r]) >= 'a' && tolower(s[r])<='z')){
                r--;
                continue;
            }
            else if (tolower(s[l]) != tolower(s[r])){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};