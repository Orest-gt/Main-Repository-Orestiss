from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(start: Node) -> None:
    if not root:
        return
    queue = deque([start])
    print("|", end=" ")

    while queue:
        node = queue.popleft()
        print(node.value, end=" | ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.left)

root = Node(20)
root.left = Node(30)
root.right = Node(10)

bfs(root)