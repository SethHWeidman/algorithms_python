from collections import defaultdict
from graph import Graph
import pickle
import sys

def main():
    sys.setrecursionlimit(0x100000)
    print("Reading in text file")
    with open("SCC.txt", "r") as f:
        l = [x.strip().split(' ') for x in f.read().split('\n') if x != '']

    print("Big dictionary")
    big_dict = defaultdict(list)
    for line in l:
        big_dict[int(line[0])].append(int(line[1]))

    g4 = Graph(dict(big_dict))
    print("Computing SCCs")
    big_leaders = g4.directed_graph_sccs()

    pickle.dump(big_leaders, open("big_leaders.p", "wb"))

    return big_leaders

if __name__ == '__main__':
    main()
