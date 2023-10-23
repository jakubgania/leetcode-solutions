# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.ans = [None] * (n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ans[idKey] = value

        if self.ptr == idKey:
            if self.ans[idKey] == None:
                self.ptr += 1
                return [self.ans[idKey]]
            else:
                temp = []
                while self.ptr < len(self.ans) and self.ans[self.ptr]:
                    temp.append(self.ans[self.ptr])
                    self.ptr += 1
        
                return temp


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)