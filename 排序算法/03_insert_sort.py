"""
插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，
对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，
为最新元素提供插入空间。
"""
"""
和选择排序的区别是，选择排序在未排序的序列选出第K小的元素，放到第K的位置，
插入排序是和未排序的序列的第一个放到前面已排序序列的合适位置。
"""
def insert_sort(alist):
    n=len(alist)
    #从右边的无序序列中取出多少个
    for i in range(0,n):
        j=i
        #把从右边取出的元素放入左边有序的序列中合适的位置
        while j >0 :
            if  alist[j]<alist[j-1]:
                print(alist)
                alist[j],alist[j-1]=alist[j-1],alist[j]
            else:
                break
            j-=1
#         alist[j+1]=alist[i]
    return alist

def insert_sort1(alist):
    n=len(alist)
    for i in range(1,n):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1]=alist[j-1],alist[j]
    return alist

l1=[54,226,93,17,77,31,44,55,20]
insert_sort(l1)
# insert_sort1(l1)    