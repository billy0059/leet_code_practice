class MinStack {
public:
    vector<int> stk;
    vector<int> cur_min;
    MinStack() {
    }
    void push(int val) {
        stk.emplace_back(val);
        if (stk.size() == 1)
            cur_min.emplace_back(val);
        else{
            cur_min.emplace_back(val < cur_min.back() ? val : cur_min.back());
        }
    }

    void pop() {
        stk.pop_back();
        cur_min.pop_back();
    }

    int top() {
        return stk[stk.size()-1];
    }

    int getMin() {
        return cur_min[cur_min.size()-1];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */