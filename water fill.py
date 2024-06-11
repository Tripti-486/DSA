class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def getNode(self,data):
        newNode=Node(data)
        return newNode
    def mirror(self,r1,r2):
        if(r1==None and r2==None):
            return True
        elif(r1==None or r2==None):
            return False
        elif(r1.data!=r2.data):
            return False
        else:
            return ob.mirror(r1.left,r2.right) and ob.mirror(r1.right,r2.left)
    def bst(self,root,max,min):
        if(root==None):
            return True
        elif(root.data>=max and root.data<=min):
            return False
        
        else:
            return ob.bst(root.left,root.data,min) and \
            ob.bst(root.right,max,root.data)
def solution(box,oldcolor,newcolor,x,y):
    if(x>4 or x<0 or y>4 or y<0):
        return
    if(box[x][y]!=oldcolor):
        return
    if(box[x][y]=newcolor):
        return
    box[x][y]=newcolor                    #diagonal
    solution(box,oldcolor,newcolor,x+1,y) #x-1,y-1
    solution(box,oldcolor,newcolor,x-1,y) #x-1,y+1
    solution(box,oldcolor,newcolor,x,y+1) #x+1,y+1
    solution(box,oldcolor,newcolor,x,y-1) #x-1,y+1
       
box=[[1,1,2,1,1],
      [1,2,2,1,1],
      [2,2,2,2,2],
      [1,1,2,1,1],
      [1,1,2,1,1]]
oldcolor,newcolor,x,y=1,7,0,0   # replace all 1 with 7 and start with the coordinate 0,0
for i in range(0,5):
    for j in range(0,5):
        print(box[i][j],end='')
    print()
print()
solution

        
            
            
        

            

    
        
ob=Tree()
root1,root2=None,None
root1=ob.getNode(5)
root2=ob.getNode(5)
root1.right,root2.left=ob.getNode(6),ob.getNode(3)
root1.left,root2.right=ob.getNode(7),ob.getNode(4)
if(ob.mirror(root1,root2)==True):
    print("mirror")
else:
    print("not mirror")
if(ob.bst(root1,100,-100)==True):
    print("bst")
else:
    print("not bst")
        
