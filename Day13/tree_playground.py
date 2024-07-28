from binary_search_tree import BST
from avl_tree import AVL
if __name__ == "__main__":
    avl = AVL()

    avl.insertKey(50)
    avl.insertKey(40)
    avl.insertKey(30)

    avl.inOrderTraversal()
    avl.preOrderTraversal()
    avl.postOrderTraversal()

    avl.insertKey(60)
    avl.insertKey(70)
    avl.insertKey(80)

    avl.inOrderTraversal()
    avl.preOrderTraversal()
    avl.postOrderTraversal()
