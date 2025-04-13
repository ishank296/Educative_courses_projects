class LinkedList:
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self,data):
        newNode = self.Node(data)
        if self.head is None:
            self.head = newNode
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = newNode

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,sep=' ')
            temp = temp.next


def helper(linkedlist,head):
    if head.next is None:
        return head
    else:
        helper(linkedlist,head.next).next = head


def reverse(linkedlist):
    if linkedlist.head is None: return
    else: return helper(linkedlist,linkedlist.head)


