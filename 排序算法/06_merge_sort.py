def merge_sort(alist):
    """归并排序"""
    if len(alist)==1:
        return alist
    num=len(alist)//2
    left=merge_sort(alist[:num])
    right=merge_sort(alist[num:])
    #left和right都是有序的
    return merge(left,right)
def merge(left,right):
    l,r=0,0
    result=[]
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
#     print(result)
    result+=left[l:]
    result+=right[r:]
    return result
l1=[27,54,226,93,17,77,31,44,55,20]
l2=[27,99,0,8,13,64,86,16,7,10,88,25,90,100]
merge_sort(list(set(l1+l2)))
# merge(l1,l2)