class Tree:
    def __init__(self, data):
        self.data = data
        self.left: Tree = None
        self.right: Tree = None

    def print(self, level=0):
        ret = "\t"*level+repr(self.data)+"\n"

        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

def print_tree(root: Tree, level: int = 0):
    if root is None:
        return '\t'*level + "None" + "\n"
    
    return '\t'*level + str(root.data) + "\n" + print_tree(root.right, level+1) + print_tree(root.left, level+1)

def create_tree(arr: list[int], i: list[int]=[0]):
    j = i[0]
    i[0] += 1

    if arr[j] == '*':
        return None
    
    node = Tree(int(arr[j]))
    node.left = create_tree(arr, i)
    node.right = create_tree(arr, i)
    return node

def convert_tree_to_string(root: Tree):
    if root is None:
        return "* "

    return f"{root.data} " + convert_tree_to_string(root.left) + convert_tree_to_string(root.right)

def convert_str_to_Tree(s):
    arr = s.split()
    return create_tree(arr)

print(print_tree(convert_str_to_Tree('12 1 3 * * 2 * * 2 3 2 * * * *')))
