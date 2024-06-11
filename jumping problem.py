def sol(list,n,dp,k): #1
    if(n==0):
        return 0
    if(dp[n]!=-1):
        return dp[n]
    a=sol(list,n-1,dp,k)+abs(list[n]-list[n-1])
    for i in range(1,k+1):
        if(n-i>=0):
            b=sol(list,n-i,dp,k)+abs(list[n]-list[n-i])
            a=min(a,b)
    dp[n]=a    
    return dp[n]
list=[10,20,10,40,50]
dp=[-1]*len(list)
print(sol(list,len(list)-1,dp,3))
