from BstNode import BstNode

class BST(BstNode):
    def __init__(self, name):
        super().__init__(name)
    def insert(self, value):
        a = BST(value)
        a.right = self.right
        self.right = a

# ==================== RESTART: /Users/dgerman/Desktop/BST.py ====================
# a = BST(3)
# a.display()
# 3
# a.insert(4)
# a.display()
# 3 
#  \
#  4
# a.insert(5)
# a.display()
# 3  
#  \ 
#  5 
#   \
#   4
# a.insert(6)
# a.display()
# 3   
#  \  
#  6  
#   \ 
#   5 
#    \
#    4
# 
# ==================== RESTART: /Users/dgerman/Desktop/BST.py ====================
# a = BST(1)
# a.insert(4)
# a.insert(3)
# a.insert(2)
# a.display()
# 1   
#  \  
#  2  
#   \ 
#   3 
#    \
#    4
# 
