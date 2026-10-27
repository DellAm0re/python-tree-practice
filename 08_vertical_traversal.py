from collections import defaultdict, deque
from tree_utils import build_tree

def vertical_traversal(root):
    if root is None: return []
    columns=defaultdict(list)
    queue=deque([(root,0,0)])
    while queue:
        node,row,col=queue.popleft()
        columns[col].append((row,node.val))
        if node.left: queue.append((node.left,row+1,col-1))
        if node.right: queue.append((node.right,row+1,col+1))
    return [[value for row,value in sorted(columns[col])]
            for col in sorted(columns)]

if __name__ == '__main__':
    print(vertical_traversal(build_tree([3,9,20,None,None,15,7])))
    print(vertical_traversal(build_tree([1,2,3,4,5,6,7])))
