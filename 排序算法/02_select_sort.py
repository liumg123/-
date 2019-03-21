"""
选择排序（selection sort的工作原理是：首先在未排序的序列中找到最小（大）的元素，存到排序序列的起始位置，
然后再从剩余未排序的元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有的元素均排序完毕。）
"""
def select_sort(alist):
    n=len(alist)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if alist[min_index]>alist[j]:
                min_index=j
        alist[i],alist[min_index]=alist[min_index],alist[i]
    return alist
 
ll=[3,2,5,4,9,4,6,7,8]    
l1=[54,226,93,17,77,31,44,55,20]
select_sort(l1)