#coding:utf-8
#单向循环链表
class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem=elem
        self.next=None
class SinCycLinkedlist(object):
    """单向循环链表"""
    def __init__(self,node=None):
        self.__head=node
        if node:
            node.next=node

    
    def is_empty(self):
        """判断链表是否为空"""
        return self.__head==None

    def length(self):
        """返回链表的长度"""
        #cur游标，用来移动遍历结点
        cur=self.__head
        #count 记录数据
        if self.is_empty():
            return 0
        else:
            count=1
            while cur.next!=self.__head:
                count+=1
                cur=cur.next
            return count
        
    def travel(self):
        """遍历"""
        if self.is_empty():
            return 
        cur=self.__head
        while cur.next!=self.__head:
            print(cur.elem,end=' ')
            cur=cur.next
        #退出循环，cur指向尾结点，但尾结点的元素未打印
        print(cur.elem)
    def add(self,item):
        """在头部添加一个元素"""
        
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            cur=self.__head
            while  cur.next!=self.__head:
                cur=cur.next
            #退出循环，cur指向尾结点 
            node.next=self.__head
            self.__head=node
            cur.next=self.__head

    def append(self,item):
        """在尾部添加一个元素,尾插法"""
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            #node.next=cur.next
            node.next=self.__head
            
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
        if self.is_empty():
            return 
        
        pre=None
        cur=self.__head
        while cur.next!=self.__head:
            if cur.elem==item:
                #先判断此结点是否是头结点，如果是头结点的话
                if cur==self.__head:#pre==None
                    #头结点的情况
                    #找尾结点
                    rear=self.__head
                    while rear.next!=self.__head:
                        rear=rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next=cur.next
              
                return
            else:
                pre=cur
                cur=cur.next
        #退出循环，cur指向尾结点
        if cur.elem==item:
            if cur==self.__head:
                #链表只有一个节点
                self.__head=None
            else:
                 pre.next=self.__head
            
    def search(self,item):
        """查找结点是否存在"""
        cur=self.__head
        while cur!=self.__head: 
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        if cur.elem==item:
            return True
        else:
            return False


if __name__=='__main__':
    ll=SinCycLinkedlist()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())


    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9) # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100) # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200) # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
