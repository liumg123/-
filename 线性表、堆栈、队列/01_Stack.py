#coding:utf-8
#栈的实现
class Stack(object):
    """栈"""
    def __init__(self):
        self.__list=[]
        
    def push(self,item):
        """添加一个新元素item到栈顶"""
        self.__list.append(item)#尾部添加，时间复杂度O(1)
#         self.__list.insert(0,item)头部添加，时间复杂度O(n)
#         pass

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()
#         pass

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None
#         pass

    def is_empty(self):
        """判断栈顶是否为空"""
        return self.__list==[]
    
    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)
        
if __name__=='__main__':
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print('s.pop()',s.pop())