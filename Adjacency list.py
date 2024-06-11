class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Graph:
    def __init__(self,v):
        self.vertex=v
        self.graph=[None]*v
    def insert(self,s,d):
        newNode=Node(d)
        newNode.next=self.graph[s]
        self.graph[s]=newNode
        #newNode.next=self.Graph[d] #undirected graph
        #self.garph[s]=newNode
    def printdata(self):
        for i in range(0,4):
            temp=self.graph[i]
            while(temp!=None):
                print(i,"->",temp.data)
                temp=temp.next
    def dfs(self,v,visited=None): #dfs
        if(visited==None):
            visted=[None]*self.vertex
        print(v,end="->")
        visited[v]=1
        temp=self.graph[v]
        while(temp!=None):
            if(visited[temp.data]==None):
                
                ob.dfs(temp.data,visited)
            temp=temp.next
#no of island if it is 1
def solution(list,x,y):
    if(x<=0 or x>=4 or y<=0 or y>=4 or list[x][y]==0):
        return
    list[x][y]=0
    solution(list,x+1,y)
    solution(list,x-1,y)
    solution(list,x,y+1)
    solution(list,x,y-1)

list=[[1,1,0,0,0],
      [0,0,0,0,0],
      [0,1,0,0,1],
      [0,0,0,0,0],
      [1,0,0,1,1]];count=0
for i in range(0,5):
    for j in range(0,5):
        if(list[i][j]==1):
            count+=1
            solution(list,i,j)
       
            
            
    
        
ob=Graph(4)
ob.insert(0,1)
ob.insert(0,2);ob.insert(0,3)
ob.insert(2,3)
ob.insert(3,1)
#ob.insert(1,2)
ob.printdata()
ob.dfs(0)
print("islands",count)
 


