from tree_utils import build_tree

def max_path_sum(root):
    if root is None: raise ValueError('tree must not be empty')
    best=float('-inf')
    down={None:0}
    stack=[(root,False)]
    while stack:
        node,visited=stack.pop()
        if not node: continue
        if not visited:
            stack.append((node,True))
            stack.append((node.right,False))
            stack.append((node.left,False))
        else:
            left=max(0,down[node.left]); right=max(0,down[node.right])
            best=max(best,node.val+left+right)
            down[node]=node.val+max(left,right)
    return best

if __name__ == '__main__':
    print(max_path_sum(build_tree([1,2,3])))
    print(max_path_sum(build_tree([-10,9,20,None,None,15,7])))
