class CustomStack:
    def __init__(self) -> None:
        self.stack = []
        self.increment = []
    
    def push(self, v: int) -> None:
        self.stack.append(v)
        self.increment.append(0) 
        print(self.stack[-1])
    
    def pop(self) -> None:
        if not self.stack:
            print("EMPTY")
            return

        if len(self.stack) > 1:
            self.increment[-2] += self.increment[-1]
        self.stack.pop()
        self.increment.pop()
        self.print_top()
    
    def inc(self, i: int, v: int) -> None:
        # Considering the common operations on the data types of the stack, use delayed updates and increment when you need to get the value at the top of the stack
        if self.stack:
            self.increment[min(i, len(self.stack)) - 1] += v
        self.print_top()

    def print_top(self) -> None:
        if not self.stack:
            print('EMPTY')
        else:
            print(self.stack[-1] + self.increment[-1])

