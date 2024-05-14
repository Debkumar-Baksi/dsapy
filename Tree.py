import queue
class tree:
    class BinaryTree:
        class Node:
            def __init__(self, key):
                self.key = key
                self.left = None
                self.right = None

        @staticmethod
        def insert(root, key):
            if not root:
                return tree.BinaryTree.Node(key)
            if key < root.key:
                root.left = tree.BinaryTree.insert(root.left, key)
            elif key > root.key:
                root.right = tree.BinaryTree.insert(root.right, key)
            return root

        @staticmethod
        def delete(root, key):
            if not root:
                return root
            if key < root.key:
                root.left = tree.BinaryTree.delete(root.left, key)
            elif key > root.key:
                root.right = tree.BinaryTree.delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                min_node = tree.BinaryTree.find_minimum(root.right)
                root.key = min_node.key
                root.right = tree.BinaryTree.delete(root.right, min_node.key)
            return root

        @staticmethod
        def find_minimum(node):
            while node.left:
                node = node.left
            return node

        @staticmethod
        def find_max(node):
            while node.right:
                node = node.right
            return node

        class traverse:
            @staticmethod
            def inorder_traversal(root):
                result = []
                if root:
                    result.extend(tree.BinaryTree.traverse.inorder_traversal(root.left))
                    result.append(root.key)
                    result.extend(tree.BinaryTree.traverse.inorder_traversal(root.right))
                return result

            @staticmethod
            def preorder_traversal(root):
                result = []
                if root:
                    result.append(root.key)
                    result.extend(tree.BinaryTree.traverse.preorder_traversal(root.left))
                    result.extend(tree.BinaryTree.traverse.preorder_traversal(root.right))
                return result

            @staticmethod
            def postorder_traversal(root):
                result = []
                if root:
                    result.extend(tree.BinaryTree.traverse.postorder_traversal(root.left))
                    result.extend(tree.BinaryTree.traverse.postorder_traversal(root.right))
                    result.append(root.key)
                return result

        @staticmethod
        def view_tree(root):
            if not root:
                return
            q = queue.simple
            q.enqueue(root)
            while q.size() > 0:
                level_size = q.size()
                for _ in range(level_size):
                    node = q.dequeue()
                    print(node.key, end=" ")
                    if node.left:
                        q.enqueue(node.left)
                    if node.right:
                        q.enqueue(node.right)
                print()
    class BinarySearchTree:
        class Node:
            def __init__(self, key):
                self.key = key
                self.left = None
                self.right = None

        @staticmethod
        def insert(root, key):
            if not root:
                return tree.BinarySearchTree.Node(key)
            if key < root.key:
                root.left = tree.BinarySearchTree.insert(root.left, key)
            elif key > root.key:
                root.right = tree.BinarySearchTree.insert(root.right, key)
            return root

        @staticmethod
        def delete(root, key):
            if not root:
                return root
            if key < root.key:
                root.left = tree.BinarySearchTree.delete(root.left, key)
            elif key > root.key:
                root.right = tree.BinarySearchTree.delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                min_node = tree.BinarySearchTree.find_minimum(root.right)
                root.key = min_node.key
                root.right = tree.BinarySearchTree.delete(root.right, min_node.key)
            return root

        @staticmethod
        def find_minimum(node):
            while node.left:
                node = node.left
            return node

        @staticmethod
        def find_max(node):
            while node.right:
                node = node.right
            return node

        class traverse:
            @staticmethod
            def inorder_traversal(root):
                result = []
                if root:
                    result.extend(tree.BinarySearchTree.traverse.inorder_traversal(root.left))
                    result.append(root.key)
                    result.extend(tree.BinarySearchTree.traverse.inorder_traversal(root.right))
                return result

            @staticmethod
            def preorder_traversal(root):
                result = []
                if root:
                    result.append(root.key)
                    result.extend(tree.BinarySearchTree.traverse.preorder_traversal(root.left))
                    result.extend(tree.BinarySearchTree.traverse.preorder_traversal(root.right))
                return result

            @staticmethod
            def postorder_traversal(root):
                result = []
                if root:
                    result.extend(tree.BinarySearchTree.traverse.postorder_traversal(root.left))
                    result.extend(tree.BinarySearchTree.traverse.postorder_traversal(root.right))
                    result.append(root.key)
                return result

        @staticmethod
        def view_tree(root):
            if not root:
                return
            q = queue.simple
            q.enqueue(root)
            while q.size() > 0:
                level_size = q.size()
                for _ in range(level_size):
                    node = q.dequeue()
                    print(node.key, end=" ")
                    if node.left:
                        q.enqueue(node.left)
                    if node.right:
                        q.enqueue(node.right)
                print()
    class AVLTree:
        class Node:
            def __init__(self, key):
                self.key = key
                self.left = None
                self.right = None
                self.height = 1

        @staticmethod
        def insert(root, key):
            if not root:
                return tree.AVLTree.Node(key)
            if key < root.key:
                root.left = tree.AVLTree.insert(root.left, key)
            else:
                root.right = tree.AVLTree.insert(root.right, key)
            root.height = 1 + max(tree.AVLTree.get_height(root.left), tree.AVLTree.get_height(root.right))
            balance = tree.AVLTree.get_balance(root)
            if balance > 1:
                if key < root.left.key:
                    return tree.AVLTree.rotate_right(root)
                else:
                    root.left = tree.AVLTree.rotate_left(root.left)
                    return tree.AVLTree.rotate_right(root)
            if balance < -1:
                if key > root.right.key:
                    return tree.AVLTree.rotate_left(root)
                else:
                    root.right = tree.AVLTree.rotate_right(root.right)
                    return tree.AVLTree.rotate_left(root)
            return root

        @staticmethod
        def delete(root, key):
            if not root:
                return root
            if key < root.key:
                root.left = tree.AVLTree.delete(root.left, key)
            elif key > root.key:
                root.right = tree.AVLTree.delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                min_node = tree.AVLTree.find_minimum(root.right)
                root.key = min_node.key
                root.right = tree.AVLTree.delete(root.right, min_node.key)
            if not root:
                return root
            root.height = 1 + max(tree.AVLTree.get_height(root.left), tree.AVLTree.get_height(root.right))
            balance = tree.AVLTree.get_balance(root)
            if balance > 1:
                if tree.AVLTree.get_balance(root.left) >= 0:
                    return tree.AVLTree.rotate_right(root)
                else:
                    root.left = tree.AVLTree.rotate_left(root.left)
                    return tree.AVLTree.rotate_right(root)
            if balance < -1:
                if tree.AVLTree.get_balance(root.right) <= 0:
                    return tree.AVLTree.rotate_left(root)
                else:
                    root.right = tree.AVLTree.rotate_right(root.right)
                    return tree.AVLTree.rotate_left(root)
            return root

        @staticmethod
        def find_minimum(node):
            while node.left:
                node = node.left
            return node

        @staticmethod
        def find_max(node):
            while node.right:
                node = node.right
            return node

        @staticmethod
        def get_height(root):
            if not root:
                return 0
            return root.height

        @staticmethod
        def get_balance(root):
            if not root:
                return 0
            return tree.AVLTree.get_height(root.left) - tree.AVLTree.get_height(root.right)

        @staticmethod
        def rotate_right(z):
            y = z.left
            T3 = y.right
            y.right = z
            z.left = T3
            z.height = 1 + max(tree.AVLTree.get_height(z.left), tree.AVLTree.get_height(z.right))
            y.height = 1 + max(tree.AVLTree.get_height(y.left), tree.AVLTree.get_height(y.right))
            return y

        @staticmethod
        def rotate_left(z):
            y = z.right
            T2 = y.left
            y.left = z
            z.right = T2
            z.height = 1 + max(tree.AVLTree.get_height(z.left), tree.AVLTree.get_height(z.right))
            y.height = 1 + max(tree.AVLTree.get_height(y.left), tree.AVLTree.get_height(y.right))
            return y

        class traverse:
            @staticmethod
            def inorder_traversal(root):
                result = []
                if root:
                    result.extend(tree.AVLTree.traverse.inorder_traversal(root.left))
                    result.append(root.key)
                    result.extend(tree.AVLTree.traverse.inorder_traversal(root.right))
                return result

            @staticmethod
            def preorder_traversal(root):
                result = []
                if root:
                    result.append(root.key)
                    result.extend(tree.AVLTree.traverse.preorder_traversal(root.left))
                    result.extend(tree.AVLTree.traverse.preorder_traversal(root.right))
                return result

            @staticmethod
            def postorder_traversal(root):
                result = []
                if root:
                    result.extend(tree.AVLTree.traverse.postorder_traversal(root.left))
                    result.extend(tree.AVLTree.traverse.postorder_traversal(root.right))
                    result.append(root.key)
                return result

        @staticmethod
        def view_tree(root):
            if not root:
                return
            q = queue.simple
            q.enqueue(root)
            while q.size() > 0:
                level_size = q.size()
                for _ in range(level_size):
                    node = q.dequeue()
                    print(node.key, end=" ")
                    if node.left:
                        q.enqueue(node.left)
                    if node.right:
                        q.enqueue(node.right)
                print()

    #   END OF TREE   #