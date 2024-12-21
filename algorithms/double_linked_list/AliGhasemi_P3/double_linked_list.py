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
            self.head = self.tail


    def iter(self):
        current = self.tail
        while current:
            yield current.data
            current = current.next

    def __getitem__(self, index):
        current = self.tail
        while current:
            if current.index == index:
                return current
            current = current.next
        raise IndexError("index out of range")
        
    def __setitem__(self,index, value):
        current = self.tail
        while current:
            if current.index == index:
                current.data = value
                return
            current = current.next
        raise IndexError("list assignment index out of range")
    
    def get(self, index , default = None):
        try:
            return self.__getitem__(index)
        except IndexError:
            return default
        
    def remove(self , value):
        current = self.tail
        after_current = None
        befor_current = None
        while current:
            if current.data == value:
                
                if current == self.head and current == self.tail:
                    current.next = None
                    current.prev = None
                    self.tail = None
                elif current == self.tail:
                    after_current = current.next
                    after_current.prev = None
                    self.tail = after_current
                elif current == self.head:
                    befor_current = current.prev
                    befor_current.next = None
                    self.head = befor_current
                else:
                    after_current = current.next
                    befor_current = current.prev
                    befor_current.next = after_current
                    after_current.prev = befor_current
                break
            else:
                current = current.next

    def remove_all(self, value):
        current = self.tail
        after_current = None
        befor_current = None
        while current:
            if current.data == value:
                
                if current == self.head and current == self.tail:
                    current.next = None
                    current.prev = None
                    self.tail = None
                elif current == self.tail:
                    after_current = current.next
                    after_current.prev = None
                    self.tail = after_current
                elif current == self.head:
                    befor_current = current.prev
                    befor_current.next = None
                    self.head = befor_current
                else:
                    after_current = current.next
                    befor_current = current.prev
                    befor_current.next = after_current
                    after_current.prev = befor_current
                current = befor_current.next
            else:
                current = current.next 
                

    def __delitem__(self , key):
        current = self.tail
        after_current = None
        befor_current = None
        while current:
            if current.index == key:
                
                if current == self.head and current == self.tail:
                    current.next = None
                    current.prev = None
                    self.tail = None
                elif current == self.tail:
                    after_current = current.next
                    after_current.prev = None
                    self.tail = after_current
                elif current == self.head:
                    befor_current = current.prev
                    befor_current.next = None
                    self.head = befor_current
                else:
                    after_current = current.next
                    befor_current = current.prev
                    befor_current.next = after_current
                    after_current.prev = befor_current
                break
            else:
                current = current.next

    def find(self , value):
        current = self.tail
        while current:
            if current.data == value:
                return current.index
            else: 
                current = current.next

    def swap(self , index1 , index2):
        if index1 >index2:
            print("enter the swaping indexs in assending order")
            return
        if index2 == index1:
            return
        node1 = self.get(index1)
        node2 = self.get(index2)
    
        if self.tail == node1:
            self.tail = node2
        elif self.tail == node2:
            self.tail == node1
        if self.head == node1:
            self.head = node2
        elif self.head == node2:
            self.head = node1
        
        if node1.prev == None and node2.next == None:
            node1.next.prev = node2
            node2.prev.next = node1
            node2.next = node1.next
            node1.prev = node2.prev
            node1.next = None
            node2.prev = None
        elif node1.prev == None and node2.prev == node1:
            node1.prev = node2
            node2.prev = None
            node1.next = node2.next
            node2.next = node1
            node2.next.prev = node1
        elif node2.next == None and node1.next == node2:
            node2.next = node1
            node2.prev = node1.prev
            node1.next = None
            node1.prev.next = node2
            node1.prev = node2
        elif node1.prev == None:
            temp = node1.next
            node1.next = node2.next
            node1.prev = node2.prev
            node2.prev.next = node1
            node2.next.prev = node1
            node2.next = temp
            node2.prev = None
        elif node2.next == None:
            temp = node2.prev
            node2.prev.next = node1
            node2.next = node1.next
            node2.prev = node1.prev
            node1.prev.next = node2
            node1.next.prev = node2
            node1.next = None
            node1.prev = temp
        elif node2.prev == node1:
            temp = node2.next
            node2.next.prev = node1
            node1.prev.next = node2
            node2.next = node1
            node1.next = temp
            temp = node1.prev 
            node1.prev = node2
            node2.prev = temp
        else:
            node1.next.prev = node2
            node1.prev.next = node2
            node2.next.prev = node1
            node2.prev.next = node1
            temp = node1.next
            node1.next = node2.next
            node2.next = temp
            temp = node1.prev
            node1.prev = node2.prev
            node2.prev = temp            


    def pop(self, number = 1):
        index = self.size-1
        poped_values = []
        while number > 0:
            poped_node = self.__getitem__(index)
            poped_values.append(poped_node.data)
            self.__delitem__(index)
            index -= 1
            number -= 1
        print(poped_values)
        return poped_values


    def insert(self , index , value):
        node = Node(value)
        next_index = index
        old_node = self.__getitem__(index)
        temp = old_node.prev
        old_node.prev = node
        node.next = old_node
        node.prev = temp
        node.index = index

        if old_node == self.tail:
            self.tail = node
        else:
            temp.next = node

        while next_index != self.size:
            old_node_index = self.__getitem__(next_index).index
            old_node_index += 1
            next_index += 1
        

    def get_size(self):
        print(self.size)


linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.swap(1,2)


for item in linked_list.iter():
    print(item) 
