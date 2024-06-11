def safe(maze,x,y):
    if(x>=0 and x<=4 and y>=0 and y<=4 and maze[x][y]==1):
        return True
    return False
    

def solution(maze,sol,x,y):
    
    if(x==4 and y==4 and maze[x][y]==1):
        sol[x][y]=1
        return True
    if(safe(maze,x,y)==True):
        sol[x][y]=1
        if(solution(maze,sol,x+1,y)==True):
            return True
        if(solution(maze,sol,x,y+1)==True):
            return True
        sol[x][y]=0 #tracking back to previous data
        return False
    return False
def safe(sol,r,c):
    for i in range(0,c):
        if(sol[r][i]==1):
            return False
    for i,j in zip(range(r,-1,-1),range(c,-1,-1)): #upper side diagonal
        if(sol[i][j]==1):
            return False
    for i,j in zip(range(r,5),range(c,-1,-1)): #lower side diagonal
        if(sol[i][j]==1):
            return False
    return True




def nqueen(sol,c):
    if(c>=5):
        return True
    for i in range(0,5):
        if(safe(sol,i,c)==True):
               sol[i][c]=1
               if(nqueen(sol,c+1)==True): #go for next column
                  return True
               sol[i][c]=0
    return False
maze=[[1,1,1,1,1],
      [1,0,1,0,0],
      [1,0,1,0,1],
      [0,1,1,0,1],
      [0,0,1,1,1]]
sol=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#if(solution(maze,sol,0,0)==False):
 #   print("no path")
nqueen(sol,0)
 

 
for i in range(0,5):
    for j in range(0,5):
        print(sol[i][j],end=' ')
    print()
