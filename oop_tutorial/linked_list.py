#!/usr/bin/python3

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        index = 0
        while cur.next != None:
            index = index + 1
            cur = cur.next
        return index

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)
    
    def get(self, index):
        if index >= self.length():
            print: "ERROR: 'Get' Index out of range!"
            return None
        cur_index = 0
        cur_node = self.head
        while cur_index < index:
            cur_node = cur_node.next
            cur_index = cur_index + 1
        return cur_node.data
    
    def remove(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while cur_index < index:
            last_node = cur_node
            cur_node = cur_node.next
            cur_index = cur_index + 1
        print("{} in index {} will be removed".format(cur_node.data, cur_index))
        cur_node.data = None
        last_node.next = cur_node.next
         
if __name__ == "__main__":
    my_list = linked_list()
    print("head node contains no data")
    my_list.display()
    print("Append 2nd node(index 1) which contains 1")
    my_list.append(1)
    my_list.display()
    print("length = {}".format(my_list.length()))
    print("append more")
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.display()
    print("length = {}".format(my_list.length()))
    print("element at 3rd index: {}".format(my_list.get(3)))
    print("\nNow, removing 3rd index")
    my_list.remove(3)
    my_list.display()
