import collections, sys

class TreeNode:
    def __init__(self, data=0, oddparent=None, evenparent=None):
        self.data = data
        self.oddparent = oddparent
        self.evenparent = evenparent
    
"""
Working backwards, to reach the 4-2-1 cycle at the end, we must hit a power of 2. 
There's two ways to reach a power of two:
1. A number, when divided by 2, gives you a power of two. This number then must itself be a power of two.
2. An odd number k, such that 3k+1 is a power of 2.
Let 2^n be the power of two. The odd number must then be (2^n - 1)/3
The only way to get an odd number is by halving an even number. Thus, the even number must be two times the odd number, i.e. 2(2^n -1)/3.
The candidate even numbers are 10, 42, 170, 682, 2730 etc. 
Per the conjecture, all natural numbers collapse to one of the numbers above.
"""

def build_tree(root, num_nodes):
    queue = collections.deque()

    while num_nodes > 0:
        if root.data % 2: #if odd
            root.evenparent = TreeNode(root.data*2)
            queue.append(root.evenparent)

        else: #if even
            if (root.data-1) % 3 == 0:
                root.oddparent = TreeNode(int((root.data-1)/3))
                queue.append(root.oddparent)
                num_nodes -= 1
            root.evenparent = TreeNode(root.data*2)
            queue.append(root.evenparent)

        num_nodes -= 1
        root = queue.popleft()

def preorder_ascii(node, prefix="", is_left=True, is_root=True):
    connector = "├── " if is_left else "└── "
    if is_root:
        print(f"{node.data}")
        prefix_arg = prefix
    else:
        print(f"{prefix}{connector}{node.data}")
        prefix_arg = prefix + ("│   " if is_left else "    ")
    if node.oddparent:
        preorder_ascii(node.oddparent, prefix_arg, True, False)
    if node.evenparent:
        preorder_ascii(node.evenparent, prefix_arg, False, False)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python collatzTreeBuilder.py $root_value $num_nodes")
        print("Default $root_value = 10, $num_nodes = 10")
        root_value = 10
        num_nodes = 10
    else:
        root_value = int(sys.argv[1])
        num_nodes = int(sys.argv[2])
    root = TreeNode(root_value)
    build_tree(root, num_nodes-1)
    preorder_ascii(root)