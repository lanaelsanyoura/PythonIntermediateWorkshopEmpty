import unittest
from BSTree import BSTree, TreeNode


class TestBSTree(unittest.TestCase):

    def test_addNode1(self):
        bst = BSTree()
        n = TreeNode(6)
        bst.addNode(n)
        self.assertEqual(bst.root.value, n.value)

    def test_addNode2(self):
        bst = BSTree()
        n = TreeNode(6)
        bst.addNode(n)
        bst.addNode(TreeNode(4))
        bst.addNode(TreeNode(8))
        self.assertEqual(bst.root.value, n.value)
        self.assertEqual(bst.root.left.value, 4)
        self.assertEqual(bst.root.right.value, 8)

    def test_contains(self):
        bst = BSTree()
        n = TreeNode(6)
        bst.addNode(n)
        bst.addNode(TreeNode(4))
        bst.addNode(TreeNode(8))
        self.assertTrue(8 in bst)

    def test_max(self):
        bst = BSTree()
        n = TreeNode(6)
        bst.addNode(n)
        bst.addNode(TreeNode(4, TreeNode(1), TreeNode(5)))
        bst.addNode(TreeNode(8, TreeNode(7)))
        print(bst)
        self.assertEqual(bst.get_max_value(), 8)


if __name__ == '__main__':
    unittest.main()
