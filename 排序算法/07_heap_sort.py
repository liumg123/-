def heap_sort(lst):
    def adjust(start,end):
        """最大堆调整"""
        root=start
        while True:
            child=2*root+1
            #孩子节点的索引值超过数组的最大长度
            if child>end:
                break
            #确定最大的孩子节点的索引值
            if child+1<=end and lst[child]<lst[child+1]:
                child+=1
            #孩子节点最大值和根节点进行交换
            if lst[root]<lst[child]:
                lst[root],lst[child]=lst[child],lst[root]
                root=child
            else:
                break
    #创建大根堆
    for start in range((len(lst)-2)//2,-1,-1):
        adjust(start,len(lst)-1)
    for end in range(len(lst)-1,0,-1):
        #首尾交换
        lst[0],lst[end]=lst[end],lst[0]
        #重新排序
        adjust(0,end-1)
    return lst
l1=[27,54,226,93,17,77,31,44,55,20]
l2=[27,99,0,8,13,64,86,16,7,10,88,25,90,100]
heap_sort(l1)    