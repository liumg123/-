#coding:utf-8
class Node(object):
    """结点"""
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=None):
        self.__head=node
#         node=Node()
#         pass
    def is_empty(self):
        """链表是否为空"""
        return self.__head==None
        
    def length(self):
        """链表长度"""
        #cur游标，用来移动遍历结点
        cur=self.__head
        #count 记录数据
        count=0
#         count=1#不能处理空链表
#         while cur.next!=None:
#             count+=1
#             cur=cur.nrxt
        while cur!=None:
            count+=1
            cur=cur.next
        return count
                
        
    def travel(self):
        """遍历整个链表"""
        cur=self.__head
        while cur is not  None:
            print(cur.elem,end=' ')
            cur=cur.next

            
    def add(self,item):
        """链表头部添加元素，头插法,O(1)"""
        node=Node(item)
        node.next=self.__head
        self.__head=node
       
        
        
    def append(self,item):
        """链表尾部添加元素,尾插法,O(n)"""
        node=Node(item)
        if  self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
        
    def insert(self,pos,item):
        """指定位置添加元素
        :param pos从0开始
        O(n)
        """
        if pos <= 0:#pos小于等于0，认为是头插法
            self.add(item)
        elif pos >self.length()-1:
            self.append(item)
        else:
            node=Node(item)
            pre=self.__head
            count=0
            while count<(pos-1):
                count+=1
                pre=pre.next
            #当循环推出后，pre指向pos-1位置
            node.next=pre.next
            pre.next=node
        
    def remove(self,item):
        """删除结点"""
        pre=None
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                #先判断此结点是否是头结点，如果是头结点的话
                if cur==self.__head:#pre==None
                    self.__head=cur.next
                else:
                    pre.next=cur.next
                break
            else:
                pre=cur
                cur=cur.next
            
        
        
    def search(self,item):
        """查找结点是否存在"""
        cur=self.__head
        while cur!=None: 
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False
                   
        
    

if __name__=='__main__':
    ll=SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.add(9999)
    ll.append(3)
    ll.append(4)
    ll.append(3)
    ll.append(6)
    ll.insert(-1,88)
    ll.insert(2,100)
    ll.insert(20,34)
    ll.remove(3)
    print(ll.travel())
    