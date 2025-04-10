from collections import deque
from flask import Flask, render_template, request


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


app = Flask(__name__)

def bfs(root: Node):
    queue = deque([root])
    results = []

    while queue:

        node = queue.popleft()
        results.append(node.value)

        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)

    return results

@app.route('/')
def home():
    return render_template('page.html', title="Game just started! ^:)^")

@app.route('/algos', methods=['POST', 'GET'])
def algo_page():
    if request.method == "POST":
        value_root = request.form.get('in')
        value_root_left = request.form.get('in_l')
        value_root_right = request.form.get('in_r')
        root = Node(value_root)
        root.right = Node(value_root_right)
        root.left = Node(value_root_left)
        algorithm = bfs(root)
        return render_template('algo_results.html', result=algorithm)
    return render_template('algo.html')

'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
'''

if __name__ == "__main__":
    app.run(debug=True)