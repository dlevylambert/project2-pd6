import sys

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

    def add_words(self, words):
        for word in words:
            self.add(word)

    def __contains__(self, word):
        n = self.root
        while len(word):
            p = n.array[ord(word[0])]
            if not p:
                return False
            n = p
            word = word[1:]
        return n.end

class Node(object):
    def __init__(self):
        self.array = [None for i in range(ord('z') + 1)]
        self.end = False

if __name__ == "__main__":
    ptree = Prefix_Tree()
    with open("sowpods.txt", "r") as f:
        ptree.add_words([line.rstrip() for line in f])
    print("bat" in ptree)
    print("rasdsasd" in ptree)
    print("how" in ptree)
