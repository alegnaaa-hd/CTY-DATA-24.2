class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def display(self):
        print(f"I am a Node. My key is {self.key}. my left is {self.left} my right is {self.right}")
