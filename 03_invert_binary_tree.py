from tree_utils import build_tree,tree_to_list

def invert_tree(root):
    if root is None: return None
    stack=[root]
    while stack:
        node=stack.pop()
        node.left,node.right=node.right,node.left
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return root

if __name__ == '__main__':
    for values in ([4,2,7,1,3,6,9],[2,1,3],[]):
        print(tree_to_list(invert_tree(build_tree(values))))
