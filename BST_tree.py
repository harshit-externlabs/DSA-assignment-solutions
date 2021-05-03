class BSTTree:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
            if not self.data:
                self.data = data
                return

            if self.data == data:
                return

            if data < self.data:
                if self.left:
                    self.left.insert(data)
                    return
                self.left = BSTTree(data)
                return

            if self.right:
                self.right.insert(data)
                return
            self.right = BSTTree(data)
    def print_inorder(self, datas):
        if self.left is not None:
            self.left.print_inorder(datas)
        if self.data is not None:
            datas.append(self.data)
        if self.right is not None:
            self.right.print_inorder(datas)
        return datas
    
    def print_preorder(self, datas):
        if self.data is not None:
            datas.append(self.data)
        if self.left is not None:
            self.left.print_preorder(datas)
        if self.right is not None:
            self.right.print_preorder(datas)
        return datas
    
    def print_postorder(self, datas):
        if self.left is not None:
            self.left.print_postorder(datas)
        if self.right is not None:
            self.right.print_postorder(datas)
        if self.data is not None:
            datas.append(self.data)
        return datas

bst = BSTTree()

bst.insert(7)
bst.insert(19)
bst.insert(13)
bst.insert(22)
bst.insert(10)
bst.insert(20)
bst.insert(1)
bst.insert(6)
bst.insert(25)
bst.insert(5)

print("Inorder form:")
print(bst.print_inorder([]))
print("Preorder form:")
print(bst.print_preorder([]))
print("Postorder form:")
print(bst.print_postorder([]))

