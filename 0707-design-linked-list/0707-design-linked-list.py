class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
    def get(self,index:int)->int:
        node=self.head
        while node and index>0:
            node=node.next
            index-=1
        if node:
            return node.val
        return -1

    def addAtHead(self,val:int)->None:
        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode

    def addAtTail(self,val:int)->None:
        newnode=Node(val)
        if not self.head:
            self.head=newnode
            return
        node=self.head
        while node.next:
            node=node.next
        node.next=newnode

    def addAtIndex(self,index:int,val:int)->None:
        if index==0:
            self.addAtHead(val)
            return
        newnode=Node(val)
        node=self.head
        for _ in range(index-1):
            if not node:
                return
            node=node.next
        if not node:
            return
        newnode.next=node.next
        node.next=newnode

    def deleteAtIndex(self,index:int)->None:
        if not self.head:
            return
        if index==0:
            self.head=self.head.next
            return
        node=self.head
        for _ in range(index-1):
            if not node:
                return
            node=node.next
        if node and node.next:
            node.next=node.next.next