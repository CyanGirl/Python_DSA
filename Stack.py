class Stack:

    def __init__(self):
        self.stack=[]

    def add(self,data):
        self.stack.append(data)
        return True
    
    def peek(self):
        if len(self.stack)<1:
            #no elements is there
            return False
        
        return self.stack[-1]

    def remove(self):
        if len(self.stack)<1:
            #no elements is there
            return False

        return self.stack.pop()

    def printstack(self):
        print(" ".join(self.stack))
    
def main():

    stack=Stack()
    print("\nEnter :\n    1 : To Add data\n    2 : To remove data\n    3 : To peek data\n    4 : To print\n   Any Other digit To Exit")
    choice=int(input(">>>   "))
    if choice==1:
        data=int(input("Enter Data :  "))
        stack.add(data)
    elif choice==2:
        stack.remove()
    elif choice==3:
        print(stack.peek())
    elif choice==4:
        stack.printstack()
    else:
        print("Exiting...")
        return
