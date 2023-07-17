class TimeMap:

    def __init__(self):
        self._map = {} # Set a in class member, dict.
                       # Key would be the given key,
                       # Value would be the list of [value, timestamp].

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._map:
            self._map[key] = [[value, timestamp]]
        else:
            self._map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Do binary search in self._map, since the timestamp of set are strictly increasing,
        # The timestamp in the values are already sorted when setting!
        if key not in self._map:
            return ""
        values = self._map[key]
        ret_str = ""
        l, r = 0, len(values)-1
        while l<=r:
            mid = l + (r-l)//2
            if values[mid][1] <= timestamp: # mid is valid, store the value in ret_str and
                                            # see if the timestamp could be bigger.
                    if values[mid][1] == timestamp: # This is the right answer and can be directly returned!
                        return values[mid][0]
                    ret_str = values[mid][0]
                    l = mid + 1
            else: # mid is too big, adjust the right bound
                r = mid -1
        return ret_str


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)