class linkedlist:
    class singly:
        class node:
            def __init__(self,data):
                self.data=data
                self.next=None
        head=None
        def insert_at_beginning(data):
            new_node=linkedlist.singly.node(data)
            new_node.next=linkedlist.singly.head
            linkedlist.singly.head=new_node
        def insert_at_end(data):
            new_node=linkedlist.singly.node(data)
            if not linkedlist.singly.head:
                linkedlist.singly.head=new_node
                return
            last_node=linkedlist.singly.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=new_node
        def insert_at_position(data,position):
            if position<0:
                return None
            if position==0:
                linkedlist.singly.insert_at_beginning(data)
                return
            new_node=linkedlist.singly.node(data)
            last_node=linkedlist.singly.head
            last_node_position=0
            while last_node and last_node_position<position-1:
                last_node=last_node.next
                last_node_position +=1
            if last_node is None:
                return None
            new_node.next=last_node.next
            last_node.next=new_node
        def delete_first():
            if not linkedlist.singly.head:
                return None
            linkedlist.singly.head=linkedlist.singly.head.next
        def delete_last():
            if not linkedlist.singly.head:
                return None
            if not linkedlist.singly.head.next:
                linkedlist.singly.head=None
                return
            last_node=linkedlist.singly.head
            while last_node.next.next:
                last_node=last_node.next
            last_node.next=None
        def delete_at_position(position):
            if position<0:
                return None
            if position==0:
                linkedlist.singly.delete_first()
            current_node=linkedlist.singly.head
            previous_node=None
            current_node_position=0
            while current_node and current_node_position<position:
                previous_node=current_node
                current_node=current_node.next
                current_node_position+=1
            if current_node is None:
                return None
            previous_node.next=current_node.next
        def display():
            current_node=linkedlist.singly.head
            while current_node:
                print("[{}]".format(current_node.data),end="-->")
                current_node=current_node.next
            print("[None]")

    #  END OF SINGLY LINKED LIST  #

    class doubly:
        class node:
            def __init__(self, data):
                self.data = data
                self.prev = None
                self.next = None
        head=None
        def insert_at_beginning(data):
            new_node = linkedlist.doubly.node(data)
            if linkedlist.doubly.head is not None:
                linkedlist.doubly.head.prev = new_node
            new_node.next = linkedlist.doubly.head
            linkedlist.doubly.head = new_node
        def insert_at_end(data):
            new_node = linkedlist.doubly.node(data)
            if not linkedlist.doubly.head:
                linkedlist.doubly.head = new_node
                return
            last_node = linkedlist.doubly.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node
        def insert_at_position(data, position):
            if position < 0:
                return None
            if position == 0:
                linkedlist.doubly.insert_at_beginning(data)
                return
            new_node = linkedlist.doubly.node(data)
            last_node = linkedlist.doubly.head
            last_node_position = 0
            while last_node and last_node_position < position - 1:
                last_node = last_node.next
                last_node_position += 1
            if last_node is None:
                return None
            new_node.next = last_node.next
            new_node.prev = last_node
            if last_node.next:
                last_node.next.prev = new_node
            last_node.next = new_node
        def delete_first():
            if not linkedlist.doubly.head:
                return None
            linkedlist.doubly.head = linkedlist.doubly.head.next
            if linkedlist.doubly.head:
                linkedlist.doubly.head.prev = None
        def delete_last():
            if not linkedlist.doubly.head:
                return None
            if not linkedlist.doubly.head.next:
                linkedlist.doubly.head = None
                return
            last_node = linkedlist.doubly.head
            while last_node.next.next:
                last_node = last_node.next
            last_node.next = None
        def delete_at_position(position):
            if position < 0:
                return None
            if position == 0:
                linkedlist.doubly.delete_first()
                return
            current_node = linkedlist.doubly.head
            current_node_position = 0
            while current_node and current_node_position < position:
                current_node = current_node.next
                current_node_position += 1
            if current_node is None:
                return None
            if current_node.next:
                current_node.next.prev = current_node.prev
            if current_node.prev:
                current_node.prev.next = current_node.next
        def display():
            current_node = linkedlist.doubly.head
            while current_node:
                print("[{}]".format(current_node.data), end="<-->")
                current_node = current_node.next
            print("[None]")

    #  END OF DOUBLY LINKED LIST  #

    class singly_circular:
        class node:
            def __init__(self, data):
                self.data = data
                self.next = None
        head = None
        @staticmethod
        def insert_at_beginning(data):
            new_node = linkedlist.singly_circular.node(data)
            if not linkedlist.singly_circular.head:
                new_node.next = new_node  
                linkedlist.singly_circular.head = new_node
            else:
                last_node = linkedlist.singly_circular.head
                while last_node.next != linkedlist.singly_circular.head:
                    last_node = last_node.next
                new_node.next = linkedlist.singly_circular.head
                last_node.next = new_node
                linkedlist.singly_circular.head = new_node
        @staticmethod
        def insert_at_end(data):
            new_node = linkedlist.singly_circular.node(data)
            if not linkedlist.singly_circular.head:
                new_node.next = new_node  
                linkedlist.singly_circular.head = new_node
            else:
                last_node = linkedlist.singly_circular.head
                while last_node.next != linkedlist.singly_circular.head:
                    last_node = last_node.next
                new_node.next = linkedlist.singly_circular.head
                last_node.next = new_node
        @staticmethod
        def insert_at_position(data, position):
            if position <= 0:
                return None
            if position == 1:
                linkedlist.singly_circular.insert_at_beginning(data)
                return
            new_node = linkedlist.singly_circular.node(data)
            temp = linkedlist.singly_circular.head
            for _ in range(position - 2):
                if temp.next == linkedlist.singly_circular.head:
                    return None
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        @staticmethod
        def delete_first():
            if not linkedlist.singly_circular.head:
                return None
            if linkedlist.singly_circular.head.next == linkedlist.singly_circular.head:
                linkedlist.singly_circular.head = None
            else:
                last_node = linkedlist.singly_circular.head
                while last_node.next != linkedlist.singly_circular.head:
                    last_node = last_node.next
                linkedlist.singly_circular.head = linkedlist.singly_circular.head.next
                last_node.next = linkedlist.singly_circular.head
        @staticmethod
        def delete_last():
            if not linkedlist.singly_circular.head:
                return None
            if linkedlist.singly_circular.head.next == linkedlist.singly_circular.head:
                linkedlist.singly_circular.head = None
            else:
                last_node = linkedlist.singly_circular.head
                while last_node.next.next != linkedlist.singly_circular.head:
                    last_node = last_node.next
                last_node.next = linkedlist.singly_circular.head
        @staticmethod
        def delete_at_position(position):
            if position <= 0:
                return None
            if position == 1:
                linkedlist.singly_circular.delete_first()
                return
            temp = linkedlist.singly_circular.head
            for _ in range(position - 1):
                if temp.next == linkedlist.singly_circular.head:
                    return None
                temp = temp.next
            temp.next = temp.next.next
        @staticmethod
        def display():
            if not linkedlist.singly_circular.head:
                return None
            temp = linkedlist.singly_circular.head
            while True:
                print("[{}]".format(temp.data), end=" --> ")
                temp = temp.next
                if temp == linkedlist.singly_circular.head:
                    break
            print("[Head]")

    #  END OF SINGLY CIRCULAR LINKED LIST  #

    class doubly_circular:
        class node:
            def __init__(self, data):
                self.data = data
                self.prev = None
                self.next = None
        head = None
        @staticmethod
        def insert_at_beginning(data):
            new_node = linkedlist.doubly_circular.node(data)
            if not linkedlist.doubly_circular.head:
                new_node.next = new_node  
                new_node.prev = new_node
                linkedlist.doubly_circular.head = new_node
            else:
                last_node = linkedlist.doubly_circular.head.prev
                new_node.next = linkedlist.doubly_circular.head
                new_node.prev = last_node
                linkedlist.doubly_circular.head.prev = new_node
                last_node.next = new_node
                linkedlist.doubly_circular.head = new_node
        @staticmethod
        def insert_at_end(data):
            new_node = linkedlist.doubly_circular.node(data)
            if not linkedlist.doubly_circular.head:
                new_node.next = new_node  
                new_node.prev = new_node
                linkedlist.doubly_circular.head = new_node
            else:
                last_node = linkedlist.doubly_circular.head.prev
                new_node.next = linkedlist.doubly_circular.head
                new_node.prev = last_node
                linkedlist.doubly_circular.head.prev = new_node
                last_node.next = new_node
        @staticmethod
        def insert_at_position(data, position):
            if position <= 0:
                return None
            if position == 1:
                linkedlist.doubly_circular.insert_at_beginning(data)
                return
            new_node = linkedlist.doubly_circular.node(data)
            temp = linkedlist.doubly_circular.head
            for _ in range(position - 2):
                if temp.next == linkedlist.doubly_circular.head:
                    return None
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
        @staticmethod
        def delete_first():
            if not linkedlist.doubly_circular.head:
                return None
            if linkedlist.doubly_circular.head.next == linkedlist.doubly_circular.head:
                linkedlist.doubly_circular.head = None
            else:
                last_node = linkedlist.doubly_circular.head.prev
                linkedlist.doubly_circular.head.next.prev = last_node
                last_node.next = linkedlist.doubly_circular.head.next
                linkedlist.doubly_circular.head = linkedlist.doubly_circular.head.next
        @staticmethod
        def delete_last():
            if not linkedlist.doubly_circular.head:
                return None
            if linkedlist.doubly_circular.head.next == linkedlist.doubly_circular.head:
                linkedlist.doubly_circular.head = None
            else:
                last_node = linkedlist.doubly_circular.head.prev
                last_node.prev.next = linkedlist.doubly_circular.head
                linkedlist.doubly_circular.head.prev = last_node.prev
        @staticmethod
        def delete_at_position(position):
            if position <= 0:
                return None
            if position == 1:
                linkedlist.doubly_circular.delete_first()
                return
            temp = linkedlist.doubly_circular.head
            for _ in range(position - 1):
                if temp.next == linkedlist.doubly_circular.head:
                    return None
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        @staticmethod
        def display():
            if not linkedlist.doubly_circular.head:
                return None
            temp = linkedlist.doubly_circular.head
            while True:
                print("[{}]".format(temp.data), end=" <--> ")
                temp = temp.next
                if temp == linkedlist.doubly_circular.head:
                    break
            print("[Head]")

    #  END OF DOUBLY CIRCULAR LINKED LIST  #