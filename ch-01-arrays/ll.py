class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        disp = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            disp.append(cur.data)
        print(disp)

    def search(self, index):
        cur_idx = 0
        cur_node = self.head
        while cur_node.next!= None:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def delete(self, index):
        cur_idx = 0
        cur_node = self.head
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return cur_node.data
            cur_idx += 1

    def removeDups(self):
        cur_node = last_node = self.head
        while cur_node != None:
            while last_node.next != None:
                if last_node.next.data == cur_node.data:
                    last_node.next = last_node.next.next
                else:
                    last_node = last_node.next
            cur_node = last_node = cur_node.next

ll = LinkedList()

ll.add(1)
ll.add(2)
ll.add(3)
ll.add(3)
ll.add(4)
ll.add(4)


ll.display()

# ll.search(1)
# print("The element at index is {}".format( ll.search(1)))
# print("The element at deleted is {}".format( ll.delete(1)))

ll.removeDups()
ll.display()
