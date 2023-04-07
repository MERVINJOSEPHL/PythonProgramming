class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None
    def Enqueue(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=newnode
            self.last=newnode
        else:
            self.last.next=newnode
            self.last=newnode
    def Dequeue(self):
        item=self.head.data
        if(self.head!=None and self.head.next!=None):
            self.head=self.head.next
        else:
            self.head=None
            self.last=None
        return item
    def traverse(self):
        temp=self.head
        if temp != None:
            while temp != None:
                if( temp.next != None ):
                    print(temp.data,end=',')
                else:
                    print(temp.data)
                temp=temp.next
        else:
            print('None')
ins=eval(input())
delt=int(input())
A=Queue()
for i in ins:
    A.Enqueue(i)
for j in range(delt):
    print(A.Dequeue())
A.traverse()
            
        

        
