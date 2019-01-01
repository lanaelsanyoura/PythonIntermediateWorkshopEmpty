class TreeNode:
    """
    A Node in a BST
    @param Node left: greater value
    @param Node right: lesser value
    @param value: int

    # NOTES: A leaf has None as children
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def isLeaf(self):
        """
        Return True if this node has no children (both children are None)
        @return:True if this node has no children and False otherwise
        """
        return self.left is None and self.right is None


class BSTree():
    """
    A Binary search tree such with a root TreeNode such that the value
    of the TreeNode is greater than or equal to all the values in its
    left subtree, and less than or equal to the values in the right subtree
                 ____(8)____
                |           |
             __(4)      __(10)__
            |          |        |
           (1)        (9)     (11)

    ==== Attributes ====

    root: TreeNode, default is None
    size: number of nodes in our tree
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def addNode(self, node):
        """
        Add a node to our tree while keeping the BST ordering
        @param node:
        @return:
        """
        self.root = self.add_helper(self.root, node)

    def add_helper(self, currNode, nodeToAdd):
        """
        Add the nodeToAdd to this currNode's children
        @param currNode: Could be None, node we're on
        @param nodeToAdd: Node to ad
        @return: the modified currNode after adding nodeToAdd
        """
        # Recursively build this tree
        self.size += 1
        if currNode is None:
            return nodeToAdd
        if nodeToAdd.value <= currNode.value:
            currNode.left = self.add_helper(currNode.left, nodeToAdd)
        elif nodeToAdd.value >= currNode.value:
            currNode.right = self.add_helper(currNode.right, nodeToAdd)
        return currNode

    def __str__(self):
        """
        Read left subtree, read root, read right subtree
        Prints the values in ascending order
        :return:
        """
        return self.str_helper(self.root)

    def str_helper(self, currNode):
        """
        Print the values in the tree through in-order
        :param currNode: The node we are currently on
        :return: The string representing this node
        """
        if currNode is not None:
            return "{} {} {}".format(self.str_helper(currNode.left), currNode.value, self.str_helper(currNode.right))
        return ""

    def __contains__(self, value):
        """
        Check if value is in this Tree
        @param value: int value of node we're looking for
        @return: True if value in self, else False
        """
        return self.contains_helper(value, self.root)

    def contains_helper(self, value, currNode):
        """
        Helper function that checks if value is in a currNode or its subtrees
        @param value: int
        @param currNode: TreeNode
        @return: True if value in currNode, else False
        """
        # Check to see if this BST contains the given value
        if currNode is None:
            return False
        if value == currNode.value:
            return True
        if value < currNode.value:
            return self.contains_helper(value, currNode.left)
        if value > currNode.value:
            return self.contains_helper(value, currNode.right)

    def get_max_value(self):
        """
        Return the max value in our tree
        @return: int
        """
        return self.get_max_helper(self.root)

    def get_max_helper(self, currNode):
        """
        Return the max value in currNode
        @param currNode: TreeNode
        @return: int
        """
        if currNode.isLeaf():
            return currNode.value
        if currNode.right is None:
            return max(currNode.value, self.get_max_helper(currNode.left))
        return self.get_max_helper(currNode.right)


