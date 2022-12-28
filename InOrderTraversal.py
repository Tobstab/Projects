# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(root):
    stack=[]
    travel=[]
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop(-1)
            travel.append(current.val)
            current = current.right
        else:
            break

            
                
    return travel