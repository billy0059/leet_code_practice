class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (const auto& c : s){
            if (c=='(' || c=='{' || c=='['){
                stk.push(c);
            }
            else if (c == ')'){
                if (stk.size() == 0) return false;
                if (stk.top() != '(') return false;
                stk.pop();
            }
            else if (c == '}') {
                if (stk.size() == 0) return false;
                if (stk.top() != '{') return false;
                stk.pop();
            }
            else if (c == ']'){
                if (stk.size() == 0) return false;
                if (stk.top() != '[') return false;
                stk.pop();
            }
        }
        if (stk.size() > 0)
            return false;
        return true;
    }
};