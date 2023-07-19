class MinStack:

    def __init__(self):
        self._list = []
        # Store min val using another list, which list[index] stores the minimum val at that point in the stack
        self.min_list = []

    def push(self, val: int) -> None:
        self._list.append(val)
        if len(self._list) == 1:
            self.min_list.append(val)
        else:
            if val < self.min_list[-1]:
                self.min_list.append(val)
            else:
                self.min_list.append(self.min_list[-1])

    def pop(self) -> None:
        self._list.pop()
        self.min_list.pop()

    def top(self) -> int:
        return self._list[-1]

    def getMin(self) -> int:
        return self.min_list[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()