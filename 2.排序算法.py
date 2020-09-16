'''
def bubble_sort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j+1]<alist[j]:
                 alist[j+1],alist[j]=alist[j],alist[j+1]
    return alist
def  choose_sort(alist):
    for i in range(len(alist)-1,0,-1):
        b=0
        for j in range(1,i+1):
            if alist[b]<alist[j]:
                b=j
        alist[b],alist[j]=alist[j],alist[b]
    return alist

def insertion_sort(alist):
    for i in range(1,len(alist)):
        b=alist[i]
        while i>0 and b<alist[i-1]:
            a[i]=a[i-1]
            i=i-1
        alist[i],b=b,alist[i]
    return alist

def quick_sort(alist,first,last):
    if first<last:
        pivot=alist[first]
        left=first+1
        right=last
        while right >=left  :
            while left <=right and alist[left]<=pivot:
                left+=1
            while left <= right and  alist[right]>=pivot:
                right-=1
            if right > left:
                alist[left],alist[right]=alist[right],alist[left]
        alist[first],alist[right]=alist[right],alist[first]
        splitpoint=right
        quick_sort(alist,first,splitpoint-1)
        quick_sort(alist,splitpoint+1,last)
alist=[1,5,6,8,9,2,4,3,6]
quick_sort(alist,0,len(alist)-1)
print(alist)
'''