from tree_utils import build_tree

def min_camera_cover(root):
    # 0: uncovered; 1: camera; 2: covered without camera
    state={None:2}
    cameras=0
    stack=[(root,False)]
    while stack:
        node,visited=stack.pop()
        if node is None: continue
        if not visited:
            stack.append((node,True))
            stack.append((node.right,False))
            stack.append((node.left,False))
        else:
            left,right=state[node.left],state[node.right]
            if left==0 or right==0:
                state[node]=1
                cameras+=1
            elif left==1 or right==1:
                state[node]=2
            else:
                state[node]=0
    if root and state[root]==0: cameras+=1
    return cameras

if __name__ == '__main__':
    print(min_camera_cover(build_tree([0,0,None,0,0])))
    print(min_camera_cover(build_tree([0,0,None,0,None,0,None,None,0])))
