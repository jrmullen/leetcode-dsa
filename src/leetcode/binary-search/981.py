class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        answer = ""
        if key not in self.keys:
            return answer
        else:
            l = 0
            r = len(self.keys[key]) - 1
            while l <= r:
                m = (l + r) // 2

                if self.keys[key][m][1] == timestamp:
                    return self.keys[key][m][0]
                elif self.keys[key][m][1] <= timestamp:
                    answer = self.keys[key][m][0]
                    l = m + 1
                else:
                    r = m - 1
            return answer


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
