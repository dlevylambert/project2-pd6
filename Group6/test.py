import time, trie, sys
start = time.clock()
ptree = trie.Prefix_Tree()
with open("sowpods.txt", "r") as f:
    ptree.add_words([word.rstrip("\n") for word in f])
print(time.clock() - start)
print(sys.getsizeof(ptree))
