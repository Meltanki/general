class AVLNode:
    def __init__(self, parent, val=0, left=None, right=None):
        self.parent = parent
        self.val = val
        self.height = 0
        self.left = left
        self.right = right
        
class AVLTree:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        new_node = AVLNode(None,val)
        # If inserting into an empty tree
        if not self.root: self.root = new_node
        
        find_parent = self.root
        
        while find_parent != None:
            if find_parent.val > val:
                if not find_parent.left:
                    new_node.parent = find_parent
                    find_parent.left = new_node
                    break
                else:
                    find_parent = find_parent.left
            elif find_parent.val < val:
                if not find_parent.right:
                    new_node.parent = find_parent
                    find_parent.right = new_node
                    break
                else:
                    find_parent = find_parent.right
            else:
                return
            
        self._rebalance(new_node)
        
    def _height(self, node):
        if not node: return -1
        else: return node.height
    
    def delete(self, val):
        pass
        
    def _rebalance(self, node):
        while node is not None:
            node.height = max(self._height(node.left),self._height(node.right))+1
            # if left heavy
            if self._height(node.left)-self._height(node.right)>1:
                if self._height(node.left.left) > self._height(node.left.right):
                    self._right_rotate(node)
                else:
                    self._left_rotate(node.left)
                    self._right_rotate(node)
            # if right heavy
            elif self._height(node.right)-self._height(node.left)>1:
                if self._height(node.right.right) > self._height(node.right.left):
                    self._left_rotate(node)
                else:
                    self._right_rotate(node.right)
                    self._left_rotate(node)
            node = node.parent
        
    def _left_rotate(self, node):
        right = node.right
        right.parent = node.parent
        if not node.parent:
            self.root = right
        else:
            if node.parent.left is node:
                node.parent.left = right
            elif node.parent.right is node:
                node.parent.right = right
        node.right = right.left
        if node.right: node.right.parent = node
        right.left = node
        node.parent = right
        node.height = max(self._height(node.left),self._height(node.right))+1
        right.height = max(self._height(right.left),self._height(right.right))+1
    
    def _right_rotate(self, node):
        left = node.left
        left.parent = node.parent
        if not node.parent:
            self.root = left
        else:
            if node.parent.left is node:
                node.parent.left = left
            elif node.parent.right is node:
                node.parent.right = left
        node.left = left.right
        if node.left: node.left.parent = node
        left.right = node
        node.parent = left
        node.height = max(self._height(node.left),self._height(node.right))+1
        left.height = max(self._height(left.left),self._height(left.right))+1
        
    def _get_height(self, node):
        if not node: return -1
        else: return node.height
        
    def __str__(self):
        if not self.root: return '<empty tree>'
        else: 
            self.treelist = ['Tree In Order:']
            self._str(self.root)
            return ' '.join(self.treelist)
        
    def _str(self,node):
        if node.left: self._str(node.left)
        self.treelist.append(str(node.val)+'('+str(node.height)+')')
        if node.right: self._str(node.right)
    
    def asciiprint(self):
        if not self.root: return '<empty tree>'

        levels = []
        
        queue = []
        queue.append((0,self.root))
        
        while(len(queue)>0):
            level,n = queue.pop(0)
            if n.left: queue.append((level+1,n.left))
            if n.right: queue.append((level+1,n.right))
            
            if len(levels)==level: levels.append([str(n.val)])
            else: levels[level].append(str(n.val))
        
        return '\n'.join([' '.join(level) for level in levels])

def test(args=None):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
        print('usage: %s <number-of-random-items | item item item ...>' % sys.argv[0])
        sys.exit()
    elif len(args) == 1:
        values = [random.randrange(100) for i in range(int(args[0]))]
        print('Order of insertion:',values)
    else:
        values = [int(i) for i in args]
        print('Order of insertion:',values)
        
    tree = AVLTree()
    print(tree)
    for val in values:
        tree.insert(val)
    print(tree)
    
    print(tree.asciiprint())
 
if __name__ == '__main__': test()  