from collections import deque
from tree_utils import TreeNode,build_tree,tree_to_list

class Codec:
    def serialize(self, root):
        if root is None: return ''
        values=[]
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if node is None:
                values.append('#')
            else:
                values.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        while values and values[-1]=='#': values.pop()
        return ','.join(values)

    def deserialize(self, data):
        if not data: return None
        parts=data.split(',')
        root=TreeNode(int(parts[0]))
        queue=deque([root]); index=1
        while queue and index<len(parts):
            node=queue.popleft()
            if index<len(parts):
                if parts[index]!='#':
                    node.left=TreeNode(int(parts[index])); queue.append(node.left)
                index+=1
            if index<len(parts):
                if parts[index]!='#':
                    node.right=TreeNode(int(parts[index])); queue.append(node.right)
                index+=1
        return root

if __name__ == '__main__':
    codec=Codec()
    for values in ([1,2,3,None,None,4,5],[],[0,-5,9,None,7]):
        data=codec.serialize(build_tree(values))
        print('Serialized:',repr(data),'Restored:',tree_to_list(codec.deserialize(data)))
