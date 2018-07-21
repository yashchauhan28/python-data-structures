class Node(object):
    def __init__(self,data,next):
        self.data = data
        self.next = next

class SingleList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def show(self):
        print("showing list")
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        
    def append(self,data):
        node = Node(data,None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self,data):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
            previous_node = current_node
            current_node = current_node.next

if __name__ == '__main__':
    ll = SingleList()
    ll.append(3)
    ll.append(4)
    ll.show()
    ll.remove(3)
    ll.show()