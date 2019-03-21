def binary_searh(alist,item):
    """二分查找，非递归版本"""
    n=len(alist)
    first=0
    last=n-1
    while first<=last:
        mid=(first+last)//2
        if alist[mid]==item:
            return True
        elif item <alist[mid]:
            last=mid-1
        else:
            first=mid+1
    return False
l1=[17,20,26,31,44,64,55,77,93,226]
l2=[0,7,8,10,13,16,25,27,64,86,88,90,99,100]
binary_search(l1,17)