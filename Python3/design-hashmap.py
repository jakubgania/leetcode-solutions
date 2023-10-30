# https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        self.arr = []
        

    def put(self, key: int, value: int) -> None:
        flg = False

        if self.arr:
            counter = 0
            for item in self.arr:
                if item[0] == key:
                    flg = True
                    self.arr[counter][1] = value
                    break
                    
                counter += 1
            
            if not flg:
                self.arr.append([key, value])

        else:
            self.arr.append([key, value])

    def get(self, key: int) -> int:
        flg = False

        if self.arr:
            for item in self.arr:
                if item[0] == key:
                    return item[1]

            else:
                return -1
        else:
            return -1
        
    def remove(self, key: int) -> None:
        counter = 0

        if self.arr:
            for item in self.arr:
                if item[0] == key:
                    self.arr.pop(counter)
                
                counter += 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)