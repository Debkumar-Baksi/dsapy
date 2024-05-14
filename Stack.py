class stack:
    def __init__(self):
        self.items = []
    @staticmethod
    def push(item):
        stack.items.append(item)
    @staticmethod
    def pop():
        if stack.items:
            return stack.items.pop()
        else:
            return None
    @staticmethod
    def view():
        n=len(stack.items)
        for i in range(n-1,-1,-1):
            print("---------------------")
            print("|{:>10}         |".format(stack.items[i]))
            print("---------------------")
    @staticmethod
    def peek():
        if stack.items:
            return stack.items[-1]
        else:
            return None
    @staticmethod
    def size():
        return len(stack.items)

# END OF STACK #