list1=[1,2,2,4,100,150]
list2=[0,3,5,5]
list3=[]
i=0;j=0;k=0
while(i<len(list1) and j<len(list2)):
    if(list1[i]<=list2[j]):
        list3.append(list1[i])
        i+=1
    else:
        list3.append(list2[j])
        j+=1
if(i<len(list1)):
    while(i<len(list1)):
        list3.append(list1[i])
        i+=1
else:
    while(j<len(list2)):
        list3.append(list2[j])
        j+=1
print(list3)

            
