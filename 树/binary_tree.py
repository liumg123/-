#树的实现
class Node(object):
    """树的节点"""
    def __init__(self,item):
        self.elem=item
        self.lchild=None
        self.rchild=None
    
    
class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root=None
    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
            return
        queue=[self.root]
              
        while queue:
            cur_node=queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild=node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild=node
                return
            else:
                queue.append(cur_node.rchild)
    def breadth_travel(self):
        """广度遍历,层次遍历"""
        if self.root is None:
            return
        queue=[self.root]
        while queue :
            cur_node=queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    def preorder(self,node):
        """递归实现先序遍历"""
        if node ==None:
            return
        print(node.elem,end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)
    def ineorder(self,node):
        """递归实现中序遍历"""
        if node ==None:
            return
        
        self.ineorder(node.lchild)
        print(node.elem,end=' ')
        self.ineorder(node.rchild)
    def postorder(self,node):
        """递归实现后序遍历"""
        if node ==None:
            return
        
        self.postorder(node.lchild)
#         print(root.elem)
        self.postorder(node.rchild)
        print (node.elem,end=' ')
                
tree=Tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.breadth_travel()
print('先序:')
tree.preorder(tree.root)
print('\n中序:')
tree.ineorder(tree.root)
print('\n后序:')
tree.postorder(tree.root)