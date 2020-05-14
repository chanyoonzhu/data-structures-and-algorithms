class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        former_head = self.head
        self.head = Node(val)
        self.head.next = former_head

    def includes(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def __str__(self):
        output = ""
        current = self.head
        while current:
            output += ("{ " + current.val + " } -> ")
            current = current.next
        output += "NULL"
        return output

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

cities = LinkedList()
cities.insert("Beijing")
cities.insert("Guangzhou")
cities.insert("Chengdu")
print(cities)