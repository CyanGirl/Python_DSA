class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None

    def printList(self):
        value=self.head

        while(value):
            print(value.data)
            value=value.next

    def insertBeg(self,newData):
        newNode=Node(newData)       #creating new node
        
        if self.head!=None:         #checking if the list is non empty
            newNode.next=self.head

        self.head=newNode

    def insertEnd(self,newData):
        newNode=Node(newData)

        if self.head==None:         #if the list is empty
            self.head=newNode
        else:
            temp=self.head
            while(temp.next!=None):     #traverse till the end
                temp=temp.next
            temp.next=newNode

    def insertAfter(self,prevData,newData):
        newNode=Node(newData)

        if self.head==None:
            print("Oops! There is no Existing List...")
        else:
            flag=False
            temp=self.head
            while(temp!=None):
                if temp.data==prevData:
                    flag=True
                    break
                temp=temp.next
            if flag==False:
                print("No Such Data exists!")
            else:
                newNode.next=temp.next
                temp.next=newNode
    
    def deleteBeg(self):
        temp=self.head
        if temp.next==None:
            self.head=None
        else:
            self.head=temp.next
            temp.next=None

    def deleteData(self,value):
        flag=False
        if self.head==None:
            print("Empty List!")
            return
        prev=None
        curr=self.head

        while(curr!=None):
            if curr.data==value:
                flag=True
                if prev==None:
                    self.deleteBeg()
                    return
                else:
                    prev.next=curr.next
                    curr.data=None
                    curr.next=None

            prev=curr
            curr=curr.next
        
        if flag==False:
            print("The data does not exists...")

    def search(self,data):
        flag=False
        temp=self.head
        while(temp!=None):
            if temp.data==data:
                flag=True
                break
            temp=temp.next
        if flag==False:
            print("No Such Data exists!")
        else:
            print("Data Exists...")

    def detectLoop(self):
        slow=fast=self.head
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            print("There is loop")
            return
        print("There is no loop!")


if __name__=='__main__':

    linkedlist=LinkedList()
    linkedlist.printList()
