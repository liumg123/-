"""
low
"""
def quick_sort(alist,start,end):
    """快速排序"""
    if start>=end:
        return 
    low,high=start,end
    mid_value=alist[start]
    while low<high:
        #high左移，停止的条件是比基准元素小
        while low<high and alist[high]>mid_value:
            high-=1        
        #low 右移，停止的条件是比基准元素大
        while low<high and alist[low]<=mid_value:
            low+=1
        #交换逆序对
        alist[low],alist[high]=alist[high],alist[low]    
    #从循环退出时，low=high
    #把第一个元素放到合适的位置（此时的low的位置），交换位置
    alist[low],alist[start]=mid_value,alist[low]
    print(alist)
    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)
    
    return alist
l1=[54,226,93,17,77,31,44,55,20]
l2=[27,99,0,8,13,64,86,16,7,10,88,25,90,100]

quick_sort(l2,0,len(l2)-1)