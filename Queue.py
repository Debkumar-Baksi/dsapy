class queue:
    class simple:
        items = []
        @staticmethod
        def enqueue(item):
            queue.simple.items.append(item)
        @staticmethod
        def dequeue():
            if queue.simple.items:
                return queue.simple.items.pop(0)
            else:
                return None
        @staticmethod
        def view():
            n = len(queue.simple.items)
            for i in range(n):
                print("[{}]".format(queue.simple.items[i]), end=" ")
        @staticmethod
        def size():
            return len(queue.simple.items)
    class circular:
        def __init__(self , max_size):
            self.max_size=max_size
            self.items=[None]*max_size
            self.front=0
            self.rear=-1
            self.size=0
        def is_empty():
            return queue.circular.size==0
        def is_full():
            return queue.circular.size==queue.circular.max_size
        def enqueue(item):
            if not queue.circular.is_full():
                queue.circular.rear = (queue.circular.rear + 1) % queue.circular.max_size
                queue.circular.items[queue.circular.rear] = item
                queue.circular.size += 1
            else:
                return None
        def dequeue():
            if not queue.circular.is_empty():
                item = queue.circular.items[queue.circular.front]
                queue.circular.items[queue.circular.front] = None
                queue.circular.front = (queue.circular.front + 1) % queue.circular.max_size
                queue.circular.size -= 1
                return item
            else:
                return None
        def view():
            if not queue.circular.is_empty():
                idx = queue.circular.front
                for _ in range(queue.circular.size):
                    print("[{}]".format(queue.circular.items[idx]), end=" ")
                    idx = (idx + 1) % queue.circular.max_size
                print()
            else:
                return None
        def get_size():
            return queue.circular.size
        
#  END OF QUEUE  #