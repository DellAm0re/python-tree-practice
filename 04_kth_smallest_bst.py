from tree_utils import build_tree

def kth_smallest(root,k):
    stack=[]
    current=root
    while current or stack:
        while current:
            stack.append(current)
            current=current.left
        current=stack.pop()
        k-=1
        if k==0: return current.val
        current=current.right
    raise ValueError('k exceeds number of nodes')

if __name__ == '__main__':
    print(kth_smallest(build_tree([3,1,4,None,2]),1))
    print(kth_smallest(build_tree([5,3,6,2,4,None,None,1]),3))
