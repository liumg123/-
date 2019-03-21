#coding:utf-8
#双端队列的实现
class DeQueue(object):
    """双端队列"""
    def __init__(self):
        self.__list=[]
        
    def add_front(self,item):
        """往队列中添加一个元素"""
        self.__list.insert(0,item)
        
    def add_rear(self,item):
        """从队列尾部添加一个元素"""
        self.__list.append(item)
        
    def pop_front(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)
    
    def pop_rear(self):
        """从队列尾部删除一个元素"""
        return self.__list.pop()

    def is_empty(self):
        return self.__list==[]
    
    def size(self):
        """返回队列的大小"""
        return len(self.__list)
if __name__=='__main__':
    s=DeQueue()
    s.add_front(1)
    s.add_front(2)
    s.add_rear(3)
    s.add_rear(4)
    print('s.pop_front()',s.pop_rear())