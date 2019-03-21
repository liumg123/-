#冒泡排序
def bubble_sort(alist):
    for k in range(len(alist)-1):
        count=0
        for i in range(len(alist)-k-1):
            j=i+1
            if alist[i]>alist[j]:
                count+=1
                alist[j],alist[i]=alist[i],alist[j]
        if count==0:#在某次过程中没有进行交换，序列有序的，退出
            return alist
    return alist
bubble_sort([3,2,5,4,9,4,6,7,8])
