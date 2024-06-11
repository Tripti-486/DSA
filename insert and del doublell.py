class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class List:
    def __init__(self):
        self.head=None
    def insertend(self,data):
        newnode=Node(data)
        if(self.head==None):
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp
    def insertfront(self,data):
        temp=self.head
        newnode=Node(data)
        self.head=newnode
        newnode.next=temp
        temp.prev=newnode
    def insertpos(self,data,pos):
        newnode=Node(data)
        t1.self.head
        t2=t1.next
        while(pos>2):
            t1=t1.next
            pos-=1
        t2=t1.next
        t1.next=newnode
        newnode.next=t2
        t2.prev=newnode
        newnode.prev=t1
            
        
    def deletefront(Self):
        temp=self.head          #self.head=self.head.next
        self.head=temp.next
        self.head.prev=None
        temp=None
    def deletepos(self,pos):
        t1.self.head
        
        while(pos>2):
            t1=t1.next
            pos-=1
        t2=t1.next
        t1.next=t2.next
        t2=None
        
        
    def deletelast(Self):
        t1=self.head           #t1=self.head
        
        t2=t1.next              #while(t1.next.next!=None)
        
        while(t2.next!=None):   #t1=t1.next
                                #t2=t1.next
                                #t1.next=None
            t1=t1.next
            t2=t2.next
        t1.next=None
        t2=None
        
    def display(self):
        
        temp=self.data
        while(temp!=None):
            print(temp.data)
            temp=temp.next
ob=List()
ob.insertend(10)
ob.insertend(20)
ob.insertfront(20)
