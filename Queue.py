class Queue:
    
    
    def __init__(self,size):
        self.size=size
        self.queue=[None for _ in range(size)]
        self.front,self.rear=0,0
        
    def isEmpty(self):
        return (True if self.front==self.rear else False)
    
    def isFull(self):
        return (True if self.rear==self.size else False)
    
    def enQueue(self,data):
        if self.isFull():
            return ("\t>> Queue Overflowed. <<")
        else:
            self.queue[self.rear]=data
            self.rear+=1
            return (f"\t>> Data {data} Enqueued. <<")
        
    def deQueue(self):
        if self.isEmpty():
            return ("\t>> Queue Underflowed. <<")
        else:
            data=self.queue[self.front]
            self.queue[self.front]=None
            self.front+=1
            return (f"\t>> Data {data} dequeued. <<")
        
    def printQueue(self):
        if self.isEmpty():
            return ("\t>> Queue is Empty <<")
        else:
            temp=list(map(str,self.queue))
            QueueStr="  ".join(temp)
            return (f"\t>> The Queue is:\n {QueueStr} <<")
        
    def peekFront(self):
        return ("\t>> Queue is Empty <<" if self.isEmpty else self.queue[self.front])
    
    def peekRear(self):
        return ("\t>> Queue is Empty <<" if self.isEmpty else self.queue[self.rear])
        

if __name__=="__main__":
    size=int(input("Enter Size of Queue: \n>>  "))
    obj=Queue(size)
    
    while True:
        print("\n\nEnter :\n    1 : To Add data\n    2 : To remove data\n    3 : To peek Front & Rear\n    4 : To print\n   Any Other digit To Exit")
        choice=int(input(">>>   "))
        if choice==1:
            data=int(input("Enter Data :  "))
            print(obj.enQueue(data))
        elif choice==2:
            print(obj.deQueue())
        elif choice==3:
            print("The Front is with: ",obj.peekFront())
            print("The Rear is with: ",obj.peekRear())
        elif choice==4:
            print(obj.printQueue())
        else:
            print("\n\nExiting...")
            break
            
