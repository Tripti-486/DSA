def part_t(arry,lw,hg):
    pivot = arry[hg]
    i=lw-1
    for j in range(lw,hg):
        if arr[j] <= pivot:
            i=i+1
            (arry[i],arry[j])=(arry[j],arry[i])
        (arry[i+1],arry[hg])=(arry[hg],arry[i+1])
        return i+1
def qk_sort(arry,lw,hg):
    if lw < hg:
        p1=part_t(arry,lw,hg)
        qk_sort(arry,lw,pi-1)
        qk_sort(arry,hg,pi+1)
def part_t(arry,lw,hg):
    pivot=arry[hg]
    i=lw-1
    for j in range(lw,hg):
        if arry[j] <= pivot:
            i=i+1
        (arry[i],arry[j])=(arry[j], arry[i])
    (arry[i+1],arry[hg])=(arry[hg],arry[i+1])
    return i+1
def qk_sort(arry,lw,hg):
    if lw<hg:
        pi=part_t(arry,lw,hg)
        qk_sort(arry,lw,pi-1)
        qk_sort(arry,pi+1,hg)
data=[8,3,26,7,8]
print("Unsorted array")
print(data)
size=len(data)
qk_sort(data,0,size-1)
print('Array sorted in asc order:')
print(data)
            
