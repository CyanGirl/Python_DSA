

#each data carrying structure in a tree is called Node
class Node:
      
      #initialising a Node with Data and two pointers
      def __init__(self,data):
            self.data=data
            self.right=None
            self.left=None

      def inorderTrverseTree(self):
            
            #mid order Left -> Root -> Right
            #implementing recursions
            #if left child exists then only move to that
            if self.left:
                  self.left.inorderTrverseTree()
            print(f" {self.data} ",end=" ")
            if self.right:
                  self.right.inorderTrverseTree()

      def preorderTraversal(self):
            if self.data:
                  print(f" {self.data} ",end=" ")
            if self.left:
                  self.left.preorderTraversal()
            if self.right:
                  self.right.preorderTraversal()

      def postOrderTraversal(self):
            if self.left:
                  self.left.postOrderTraversal()
            if self.right:
                  self.right.postOrderTraversal()
            print(f" {self.data} ",end=" ")

      def insertNode(self,data):

            if self.right==None and self.left==None:
                  print("Both right and left are empty. \nEnter R for right insertion\nEnter L for left insertion")
                  choice=input(">>>  ")
                  if choice in "Rr":
                        self.right=Node(data)
                  elif choice in "Ll":
                        self.left=Node(data)

            elif self.right==None:
                  print("Right is empty. Inserting at it...")
                  self.right=Node(data)

            elif self.left==None:
                  print("Left is empty. Inserting at it...")
                  self.left=Node(data)

            elif self.right!=None and self.left!=None:
                  print("Both right and left are non-empty.\nEnter R for traversing to Right sub-tree\nEnter L for traversing to left sub-tree")
                  treechoice=input(">>> ")

                  #implementing recursion
                  #for loop=> while true ; self=self.right /self.left
                  
                  if treechoice in "Rr":
                        rightTree=self.right
                        #passing the next sub tree through recursion
                        rightTree.insertNode(data)

                  elif treechoice in "Ll":
                        leftTree=self.left
                        leftTree.insertNode(data)

      def printHeight(self,node):
            if node==None:
                  return 0
            else:
                  right=self.printHeight(self.right)
                  left=self.printHeight(self.left)

                  if right>left:
                        return right+1
                  else:
                        return left+1


if __name__ == "__main__":
      rootdata=input("Enter the root data :  ")
      root=Node(rootdata)
      while True:
            print("\nEnter : \n   1 : To add new node\n   2 : To traverse\n   3 : To print Height\n   Any other to exit...")
            choice=int(input(">>>  "))
            if choice==1:
                  data=input("Enter data :  ")
                  root.insertNode(data)
            elif choice==2:
                  root.inorderTrverseTree()
            elif choice==3:
                  print(root.printHeight(root))
            else:
                  break
                  exit()




"""
        -root-
  -child-   -child-
-leaf-          -leaf-
"""
#normally binarytree module already exists in Python.
#from it we can import Node and use it to make the tree
