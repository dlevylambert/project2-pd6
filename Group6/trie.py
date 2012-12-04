class Prefix_Tree(object):

    def __init__(self):
        self.root = Node()

    def add(self, word):
        n = self.root
        while len(word):
            p = n.array[ord(word[0])]
            if not p:
                p = n.array[ord(word[0])] = Node()
            n = p
            word = word[1:]
        n.end = True

    def __contains__(self, word):
        n = self.root
        while len(word):
            p = n.array[ord(word[0])]
            if not p:
                return False
            n = p
            word = word[1:]
        if n.end:
            return True
        else:
            return False

class Node(object):
    def __init__(self):
        self.array = [None for i in range(ord('z') + 1)]
        self.end = False
