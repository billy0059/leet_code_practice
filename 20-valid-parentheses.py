class Solution:
    def isValid(self, s: str) -> bool:
        # Create a list as stack
        parentheses_list = []
        for c in s:
            if c in ["(", "{", "["]:
                parentheses_list.append(c)
            else:
                if c == ")":
                    # In the if statement below, it will check the length first, and if it equals 0,
                    # it won't do the .pop() operation because we use "or" here!
                    # It will then directly return False.
                    if len(parentheses_list) == 0 or parentheses_list.pop() != "(":
                        return False
                elif c == "}":
                    if len(parentheses_list) == 0 or parentheses_list.pop() != "{":
                        return False
                elif c == "]":
                    if len(parentheses_list) == 0 or parentheses_list.pop() != "[":
                        return False
        return True if len(parentheses_list) == 0 else False