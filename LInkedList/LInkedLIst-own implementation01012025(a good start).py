class node:
    def __init__(self,data):
        self.data=data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head=None
    def addAtLast(self,data):
        newnode=node(data)
        if not self.head:
            self.head=newnode
            return
        itr = self.head
        while itr.next != None:
            itr=itr.next
        itr.next=newnode
    def add(self,data,pos=None):
        newnode=node(data)
        if not pos:
            self.addAtLast(data)
            return
        itr=self.head
        while itr:
            if itr.data == pos:
                break
            itr=itr.next
        if not itr:
            print(data,'position not found')
            return
        newnode.next=itr.next
        itr.next=newnode
        return
    def remove(self,data):
        if not self.head:
            print('sorry the list is empty')
            return
        if self.head.data == data:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next:
            dt=itr.next.data
            if itr.next.data == data:
                itr.next=itr.next.next
                return
            itr=itr.next
        print('data not found')
        return 
        
    def display(self):
        if not self.head:
            print('empty list')
            return
        itr=self.head
        while itr:
            print(itr.data,'->',end='')
            itr=itr.next
        print('\n')
            
ll=LinkedList()
ll.addAtLast(1)
ll.addAtLast(2)
ll.addAtLast(3)
ll.add(5,1)
ll.display()
# ll.remove(5)
ll.remove(3)
ll.display()


