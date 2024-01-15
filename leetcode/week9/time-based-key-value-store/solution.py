class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key) is None:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if self.store.get(key) is None:
            return ""
        arr = self.store[key]
        l, r = 0, len(arr) - 1
        latestValue = ""
        while (l <= r):
            m = l + (r - l) // 2
            time, value = arr[m]
            if time == timestamp:
                return value
            if time > timestamp:
                r = m - 1
            else:
                l = m + 1
                latestValue = value
        return latestValue

    # Time: O(1) in set op, O(log(n)) in get op
    # Space: O(n) in worse case
    # n is number of operations


def run(ops, inps):
    obj = TimeMap()
    out = [None]
    for i in range(1, len(ops)):
        inp = inps[i]
        if ops[i] == "set":
            out.append(obj.set(inp[0], inp[1], inp[2]))
        else:
            out.append(obj.get(inp[0], inp[1]))
    print(out)


ops = ["TimeMap", "set", "get", "get", "set", "get", "get"]
inps = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3],
        ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
run(ops, inps)

ops = ["TimeMap", "set", "set", "set", "set", "set", "get"]
inps = [[], ["foo", "bar", 1], ["foo", "bar2", 2], ["foo", "bar4", 4],
        ["foo", "bar6", 6], ["foo", "bar7", 7], ["foo", 5]]
run(ops, inps)

# store
# {
#   "foo": [(1, "bar"), (4, "bar2")]
# }

# l = 1
# r = 1
# m = 1
# latestValue = "bar2"
# timestamp = 4

# out = [None, None, "bar", "bar", "bar2"]
