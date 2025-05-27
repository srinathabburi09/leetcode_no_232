class MyQueue:

    def __init__(self):
        self.s1 = []   #pushing stack            # lets say s1  = [1,2,3,4] and s2 = [4,3,2,1]  so the appending elements in s1 will be the same elements popping from the s1 and appending in s2 and by poppoing elements from s2 will be the queue
        self.s2 = []    #pop stack
    def push(self, x: int) -> None:
        self.s1.append(x) #append x in to pushing stack
    def pop(self) -> int:
        if not self.s2:    #poping from s1 to append into s2 and so to make a pop from s2 which leads to queue implemetation
            while self.s1:  
                self.s2.append(self.s1.pop())
        return self.s2.pop()
    def peek(self) -> int:  #peek element is the top most element of a data structure lets say s2's top element element == queue's first element
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
    def empty(self) -> bool:   #we return if no elements in s1 and s2 it returns true, if elements present in s1 and s2 it return to False
        return not self.s1 and not self.s2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
