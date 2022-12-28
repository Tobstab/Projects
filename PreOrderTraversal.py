# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def preorderTraversal(root):
    queue = [root]
    travel =[]
    while len(queue)>0:
        node = queue.pop()
        if node:
            travel.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
    return travel
        
