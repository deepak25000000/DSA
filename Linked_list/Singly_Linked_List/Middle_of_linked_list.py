class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Singly_linked_list:
    def __init__(self): #creating a singly linked list
        self.head = None

    def append(self, val): #adding a node at the end of the list
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traversal(self): #funtion for traveling in the linked list
        if self.head == None:
            print("Sll is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end="")
                current = current.next
                print()

    def insert_at(self, val, position): #inserting at a perticular postion in linked list
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current
    def delete(self, val):
        temp = self.head
        if temp is not None: #this loop if the value to delete is the first node 
            if temp.val == val:
                self.head = temp.next
                return
            else: #this loop if the value to delete is in between the first and last node and is the last node
                found = False
                prev = None
                while temp is not None:
                    if temp.val ==val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next = temp.next
                    return
                else:
                    print("node not found ")


def middleNode(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

sll = Singly_linked_list()
sll.append(10)
sll.append(20)
sll.append(56)
sll.append(76)
sll.insert_at(30, 2)
    
mid = middleNode(sll.head)
print("Middle node value is :", mid.val)
'''
https://leetcode.com/problems/middle-of-the-linked-list
TC = O(N)
SC = O(1)
'''