import pickle


class DSATreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return 'Value: ' + str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # function to find if value is within tree
    def find(self, value):
        if self.root:
            value = self._find_rec(value, self.root)
            if value:
                return True
            return False
        else:
            return None

    # recursive find function
    def _find_rec(self, value, curr):
        if value > curr.value and curr.right:
            return self._find_rec(value, curr.right)
        elif value < curr.value and curr.left:
            return self._find_rec(value, curr.left)
        if value == curr.value:
            return True

    # function to return height
    def height(self):
        return self._height_rec(self.root)

    # recursive height function 
    def _height_rec(self, curr):
        if curr is None:
            curr_h = -1
        else:
            left_h = self._height_rec(curr.left)
            right_h = self._height_rec(curr.right)
            if left_h > right_h:
                curr_h = left_h + 1
            else:
                curr_h = right_h + 1
        return curr_h

    # function to insert value in tree
    def insert(self, value):
        if self.root is None:
            self.root = DSATreeNode(value)
        else:
            self._insert_rec(value, self.root)

    # recursive insert method
    def _insert_rec(self, value, curr):
        if value < curr.value:
            if curr.left is None:
                curr.left = DSATreeNode(value)
            else:
                self._insert_rec(value, curr.left)

        elif value > curr.value:
            if curr.right is None:
                curr.right = DSATreeNode(value)
            else:
                self._insert_rec(value, curr.right)
        else:
            print('Current node already exists!')

    def delete(self, value):
        if self.root is None:
            self.root = DSATreeNode(value)
        else:
            self._delete_rec(value, self.root)

    def _delete_rec(self, value, curr):
        if curr is None:
            raise ValueError("ERROR: KEY NOT IN TREE")
        elif curr.value == value:
            curr = self._delete_node(value, curr)
        elif value < curr.value:
            curr.left = self._delete_rec(value, curr.left)
        else:
            curr.right = self._delete_rec(value, curr.right)

    def _delete_node(self, value, curr):
        if curr.left is None and curr.right is None:
            update_node = None
        elif curr.left is None:
            update_node = curr.right
        elif curr.right is None:
            update_node = curr.left
        else:
            update_node = BinarySearchTree._promote_succ(curr.right)
            if update_node is not curr.right:
                update_node.right = curr.right
            update_node.left = curr.left
        return update_node

    def _promote_succ(self, curr):
        succ = curr
        if curr.left is not None:
            succ = BinarySearchTree._promote_succ(curr.left)
            if succ is curr.left:
                curr.left = succ.right
        return succ

    # pre order traversal
    def pre_order(self, temp):
        if temp:
            print(temp.value)
            self.pre_order(temp.left)
            self.pre_order(temp.right)

    # inorder traversal
    def in_order(self, temp):
        if temp:
            self.in_order(temp.left)
            print(temp.value)
            self.in_order(temp.right)


    # post order traversal
    def post_order(self, temp):
        if temp:
            self.post_order(temp.left)
            self.post_order(temp.right)
            print(temp.value)

    # function to find minimum key in the tree
    def min_rec(self, curr):
        if curr.left is not None:
            min_val = self.min_rec(curr.left)
        else:
            min_val = curr.value
        return min_val

    # function to find maximum key in the tree
    def max_rec(self, curr):
        if curr.right is not None:
            max_val = self.max_rec(curr.right)
        else:
            max_val = curr.value
        return max_val

    def balance(self):
        max_height = self.height()
        balance = 1.0
        if max_height > 0:
            balance = (self.min)

    # menu function
    def menu(self):
        print('''
                ****MENU****\n
                [1] READ A CSV FILE\n
                [2] READ A SERIALIZED FILE\n
                [3] DISPLAY TREE\n
                [4] WRITE A CSV FILE\n
                [5] WRITE A SERIALIZED FILE\n
                [0] EXIT''')
        while True:
            choice = int(input('Enter an integer to select your option...\n'))
            if choice == 1:
                with open('binary_tree.csv', 'r') as f:
                    for line in f.readlines():
                        line.split(',')
                        print(line)
            elif choice == 2:
                serialized = pickle.load(open('binary_tree.p', "rb"))
                print(serialized)
            elif choice == 3:
                c = int(input('[1] Pre Order | [2] Post Order | [3] In Order\n'))
                if c == 1:
                    print(self.pre_order(self.root))
                elif c == 2:
                    print(self.post_order(self.root))
                elif c == 3:
                    print(self.in_order(self.root))
                else:
                    print('Invalid Input!')
            elif choice == 4:
                with open('binary_tree.csv', 'w') as f:
                    f.write(str(self.root))
                    f.close()
            elif choice == 5:
                print('\nSaving object to file...\n')
                try:
                    pickle.dump(self, open('binary_tree.p', "wb"))
                except:
                    print('Error: problem pickling object!')
            elif choice == 0:
                break
            else:
                print('invalid input!')


if __name__ == "__main__":
    bst = BinarySearchTree()
    '''print('Testing node creation\n')
    myNode = DSATreeNode(1)
    print(myNode)

    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(8)
    bst.insert(5)
    bst.insert(10)

    print(bst.min_rec(bst.root))
    print(bst.max_rec(bst.root))
    bst.pre_order(bst.root)
    print(bst.height())
    print(bst.find(2))
    print(bst.find(4))
    bst.delete(2)
    print(bst.find(2))'''
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(8)
    bst.insert(5)
    bst.insert(10)

    bst.menu()
