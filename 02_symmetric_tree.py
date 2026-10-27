from collections import deque
from tree_utils import build_tree

def is_symmetric(root):
    if root is None: return True
    queue = deque([(root.left, root.right)])
    while queue:
        a,b = queue.popleft()
        if a is None or b is None:
            if a is not b: return False
            continue
        if a.val != b.val: return False
        queue.append((a.left,b.right))
        queue.append((a.right,b.left))
    return True

if __name__ == '__main__':
    print(is_symmetric(build_tree([1,2,2,3,4,4,3])))
    print(is_symmetric(build_tree([1,2,2,None,3,None,3])))
