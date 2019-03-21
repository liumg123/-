def shell_sort(alist):
    """希尔排序"""
    n=len(alist)
    gap=n // 2#取折半
    while gap>=1:
    #插入算法与普通插入算法的区别就是gap的步长
        for j in range(gap,n):
            #j=[gap,gap+1,gap+2,gap+3,gap+4,......,n-1]
            i=j
            while i>0: 
                if alist[i]<alist[i-gap]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    i-=gap
                else:
                    break
        #缩短gap步长
        gap//=2
    return alist
l1=[54,226,93,17,77,31,44,55,20]
shell_sort(l1)
    