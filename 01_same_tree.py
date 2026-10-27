from tree_utils import build_tree

def is_same_tree(p, q):
    stack = [(p, q)]
    while stack:
        a, b = stack.pop()
        if a is None or b is None:
            if a is not b: return False
            continue
        if a.val != b.val: return False
        stack.append((a.left, b.left))
        stack.append((a.right, b.right))
    return True

if __name__ == '__main__':
    print(is_same_tree(build_tree([1,2,3]), build_tree([1,2,3])))
    print(is_same_tree(build_tree([1,2]), build_tree([1,None,2])))
    print(is_same_tree(build_tree([1,2,1]), build_tree([1,1,2])))
