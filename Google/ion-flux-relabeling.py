class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

    def insert(self, data):
    # Compare the new value with the parent node    
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

def constructPBT(postorder, start, h):
 
    # base case
    if start > h:
        return None
 
    # Construct the root node of the subtree formed by keys of the
    # postorder sequence in range `[start, end]`
    node = Node(2**(h)-1)
 
    # search the index of the last element in the current range of postorder
    # sequence, which is smaller than the root node's value
    i = (2**(h)-1)-(2**(h-1))
 
    # Build the right subtree before the left subtree since the values are
    # being read from the end of the postorder sequence.
 
    # recursively construct the right subtree
    node.right = constructPBT(postorder, i + 1, (2**(h)-1) - 1)
 
    # recursively construct the left subtree
    node.left = constructPBT(postorder, start, i)
 
    # return current node
    return node

def Buildtree(h):
    root=Node(2**(h)-1)
    for i in range(2**(h)-1,0,-1):
        root.insert(i) 
        
    return root.PostorderTraversal(root)

def printAncestors(root, target):    
        # Base case
        if root == None:
            return False
        
        if root.data == target:
            return True
    
        # If target is present in either left or right subtree
        # of this node, then print this node
        if (printAncestors(root.left, target) or 
            printAncestors(root.right, target)):
            print(root.data),
            return True
 
        # Else return False
        return 
        
# Calculate the depth
def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d


# Check if the tree is perfect binary tree
def is_perfect(root, d, level=0):

    # Check if the tree is empty
    if (root is None):
        return True

    # Check the presence of trees
    if (root.left is None and root.right is None):
        return (d == level + 1)

    if (root.left is None or root.right is None):
        return False

    return (is_perfect(root.left, d, level + 1) and
            is_perfect(root.right, d, level + 1))

root = Node(15)

root.left = Node(7)
root.left.right = Node(6)
root.left.left= Node(3)
root.left.right.right = Node(5)
root.left.right.left = Node(4)
root.left.left.right = Node(2)
root.left.left.left = Node(1)

root.right = Node(14)
root.right.right = Node(13)
root.right.left = Node(10)
root.right.right.right = Node(12)
root.right.right.left = Node(11)
root.right.left.right = Node(9)
root.right.left.left = Node(8)

print(root.PostorderTraversal(root))

if (is_perfect(root, calculateDepth(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
#printAncestors(root, 7)