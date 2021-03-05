# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
    
        def recursiveTrees(start, end):
            if end < start:
                return [None]
            if start == end:
                return [TreeNode(start)]
            
            trees = []
            
            for i in range(start, end+1):
                leftTrees = recursiveTrees(start, i-1)
                rightTrees = recursiveTrees(i+1, end)
                        
                for ltree in leftTrees:
                    for rtree in rightTrees:
                        trees.append(TreeNode(i, ltree, rtree))
            
            return trees
      
        return recursiveTrees(1, n)