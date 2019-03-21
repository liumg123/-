#coding:utf-8
#队列的实现
class Quene(object):
    """队列"""
    def __init__(self):
        self.__list=[]
        
    def enqueue(self,item):
        """往队列中添加一个元素"""
        self.__list.append(item)#入队频繁
#         self.__list.insert(0,item)
    
    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)
#         return self.pop()#出队频繁
    def is_empty(self):
        return self.__list==[]
    def size(self):
        """返回队列的大小"""
        return len(self.__list)
        
if __name__=='__main__':
    s=Quene()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print('s.dequeue()',s.dequeue())