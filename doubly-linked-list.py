class Node(object):
    def __init__(self,data,next,prev):
        self.data = data
        self.next = None
        self.prev = None

class DoubleList(object):
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
        node = Node(data,None,None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def remove(self,data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node is not self.head:
                    previous_node = current_node.prev
                    next_node = current_node.next

                    previous_node.next = next_node
                    next_node.prev = previous_node
                else:
                    next_node = current_node.next
                    next_node.prev = None
                    self.head = next_node
            current_node = current_node.next

if __name__ == '__main__':
    dl = DoubleList()
    dl.append(3)
    dl.append(4)
    dl.append(5)
    dl.show()
    dl.remove(4)
    dl.show()
    dl.remove(3)
    dl.show()