from tree_utils import TreeNode,tree_to_list

def recover_from_preorder(traversal):
    path=[]
    i=0
    while i<len(traversal):
        depth=0
        while i<len(traversal) and traversal[i]=='-':
            depth+=1; i+=1
        start=i
        while i<len(traversal) and traversal[i].isdigit(): i+=1
        node=TreeNode(int(traversal[start:i]))
        while len(path)>depth: path.pop()
        if path:
            parent=path[-1]
            if parent.left is None: parent.left=node
            else: parent.right=node
        path.append(node)
    return path[0] if path else None

if __name__ == '__main__':
    for s in ('1-2--3--4-5--6--7','1-2--3---4-5--6---7','1-401--349---90--88'):
        print(tree_to_list(recover_from_preorder(s)))
