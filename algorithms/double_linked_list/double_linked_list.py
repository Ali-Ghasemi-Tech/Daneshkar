class Node:
    def __init__(self, data) -> None:
        self.data= data
        self.next = None
        self.prev = None
        self.index = None
    def __str__(self) -> str:
        return str(self.data)

class LinkedList:
    
    def __init__(self) -> None:
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        node.index = self.size
        self.size += 1
        if self.head:
            self.head.next =node
            node.prev = self.head
            self.head= node
        else:
            self.tail = node
            self.head = node

    def iter(self):
        current = self.tail
        while current:
            yield current.data
            current = current.next

    def __getitem__(self, index):
        current = self.tail
        while current.next:
            if current.index == index:
                return current.data
            current = current.next
        raise IndexError
            

    def get_size(self):
        print(self.size)


linked_list = LinkedList()

linked_list.append(1)
linked_list.append("hello")
linked_list.append("m,e")
linked_list.append(6)

print(linked_list[4])
for item in linked_list.iter():
    print(item) 

