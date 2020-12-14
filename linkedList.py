class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list():
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_Node = node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next

        cur.next = new_Node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        cur = self.head
        elements = []
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)

        print(elements)

    def get(self, index):
        if index >= self.length():
            print("ERROR: Index out of range")
            return None

        cur_idx = 0
        cur = self.head

        while True:
            cur = cur.next
            if cur_idx == index:
                return cur.data
            cur_idx += 1

    def remove(self, index):
        if index >= self.length():
            print("ERROR: Index out of range")
            return None
        cur = self.head
        cur_idx = 0
        while True:
            previus = cur
            cur = cur.next
            if cur_idx == index:
                previus.next = cur.next
                return
            cur_idx += 1

    def getIndexOfElement(self, element):
        cur = self .head
        cur_idx = 0
        while cur.next != None:
            cur = cur.next
            if element == cur.data:
                return cur_idx
            cur_idx += 1
        print("ERROR: Element not found")
        return None

    def removeEle(self, element):
        cur = self .head
        cur_idx = 0
        while cur.next != None:
            previous = cur
            cur = cur.next
            if element == cur.data:
                previous.next = cur.next
                return
            cur_idx += 1
        print("ERROR: Element not found")
        return None

    def appendIncreasingOrder(self, data):
        newNode = node(data)
        print(self.length())


my_list = linked_list()
my_list.appendIncreasingOrder(5)
