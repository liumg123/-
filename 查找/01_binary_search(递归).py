#递归的方式
def binary_search(alist,item):
    """二分查找"""
    n=len(alist)
    if n>0:
        mid=n//2
        if alist[mid]==item:
            return True
        elif item <alist[mid]:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)
    return False
l1=[17,20,26,31,44,64,55,77,93,226]
l2=[0,7,8,10,13,16,25,27,64,86,88,90,99,100]
binary_search(l1,17)
    
    