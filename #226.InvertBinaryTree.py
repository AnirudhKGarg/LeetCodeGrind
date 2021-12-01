#226 invert binary tree
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root
