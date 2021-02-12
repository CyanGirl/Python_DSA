'''
This will take a count of nodes to be grouped and then alternately reverse them in a linkedlist
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def pushNode(self,data):
        if self.head==None:
            self.head=Node(data)
            return
        
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        
        temp.next=Node(data)

    def printList(self):
        if self.head==None:
            print("LinkedList is empty")
            return
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")

    def GetNodes(self,obj2,skip,count):
        if self.head==None:
            return False

        k=0
        temp=obj1.head
        data=[]

        while(k<skip and temp!=None):
            data.append(temp.data)
            temp=temp.next
            k+=1

        self.head=temp

        data=data if count%2==0 else data[::-1]
        for d in data:
            obj2.pushNode(d)
        
        

    def reverseAlter(self):
        obj2=LinkedList()
        skip=int(input("Enter the Group Count: \n>>> "))

        check=True
        count=1
        while(check!=False):
            check=obj1.GetNodes(obj2,skip,count)
            count+=1
        print("The Reverse Alternate List is:")
        obj2.printList()


obj1=LinkedList()
for i in range(1,9):
    obj1.pushNode(i)
obj1.printList()
obj1.reverseAlter()

