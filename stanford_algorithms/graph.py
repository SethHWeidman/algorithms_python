import random
from copy import deepcopy
from data_structures import Stack, Queue


class Graph():

    def __init__(self, graph):
        self.graph = graph
        self.recursive_calls = 0

    def list_of_nodes(self):
        return list(self.graph.keys())

    def choose_random_node(self):
        return random.choice(self.list_of_nodes())

    def choose_node_not_explored(self, graph, explored):
        nodes = self.list_of_nodes()
        nodes_copy = deepcopy(nodes)
        for node in explored:
            try:
                nodes_copy.remove(node) # Need try-remove statement
            except:
                pass
        if len(nodes_copy) == 0:
            return None
        return random.choice(nodes_copy)

    def bfs(self, start):
        '''
        Idea:
        Start at a node:
        Add it to a queue of nodes to be explored
        Look at all of its connections
        If they haven't been explored:
        1. Add them to an "explored" list
        2. Add them to the "to explore" queue
        Keep going until there is nothing left to explore!
        '''
        explored = []
        to_explore = Queue()

        to_explore.push(start)
        explored.append(start)

        while not to_explore.is_empty():
            el = to_explore.pop()
            new_nodes = self.graph.get(el, None)
            for node in new_nodes:
                if node not in explored:
                    explored.append(node)
                    to_explore.push(node)

        return explored

    def dfs(self, start, explored=[], new_explored=[]):
        '''
        Idea:
        Start at a node:
        Add it to a queue of nodes to be explored
        Look at all of its connections
        If they haven't been explored:
        1. Add them to an "explored" list
        2. Add them to the "to explore" queue
        Keep going until there is nothing left to explore!
        '''
        self.recursive_calls += 1
        print("Recursive calls", self.recursive_calls)
        to_explore = Stack()
        to_explore.push(start)
        if start not in new_explored:
            new_explored.append(start)
        new_nodes = self.graph.get(start, [])

        for node in new_nodes:
            if node not in new_explored + explored:
                self.dfs(node, explored, new_explored)

        return new_explored



    def shortest_path(self, node1, node2):
        '''
        Do the same thing as breadth-first search, except for each
        '''
        explored = []
        to_explore = Queue()
        distances = {}

        depth = 0
        to_explore.push(node1)
        explored.append(node1)
        distances[node1] = depth

        while not to_explore.is_empty():
            el = to_explore.pop()
            new_nodes = self.graph.get(el, None)
            for node in new_nodes:
                distances[node] = distances[el] + 1
                if node == node2:
                    return distances[node]
                if node not in explored:
                    to_explore.push(node)

        return None

    def num_connections(self):
        '''
        TODO
        '''
        # Choose starting node
        start = self.choose_random_node()
        connections = 0

        nodes = self.bfs(start)
        connections += 1

        while self.choose_node_not_explored(self.graph, nodes):
            temp = self.choose_node_not_explored(self.graph, nodes)
            new_explored = self.bfs(temp)
            nodes = nodes + new_explored
            connections += 1

        return connections

    def reverse_graph(self):
        new_graph = {}
        graph_keys = list(self.graph.keys())
        for i, node in enumerate(graph_keys):
            print("Done with", i-1, "of",
                  len(graph_keys), "iterations")
            new_graph[node] = []
            for node2 in graph_keys:
                if node in self.graph[node2]:
                    new_graph[node].append(node2)
        return new_graph

    def finishing_time(self):
        '''
        TODO
        '''
        # Choose starting node
        time = 0
        finishing_time = {}
        num_nodes = len(self.list_of_nodes())
        explored = []

        for i in list(range(num_nodes, 0, -1)):
            print("Considered", num_nodes - i,
                  "of", num_nodes, "nodes")
            if i not in explored:
                explored_temp = self.dfs(i, explored=explored, new_explored=[])
                for node in explored_temp[::-1]:
                    time += 1
                    finishing_time[node] = time
                explored = explored + explored_temp
        return finishing_time


    def directed_graph_sccs(self):
        '''
        TODO
        '''
        print("Computing finishing time")
        finishing_time = self.finishing_time()
        print("Reverse graph")
        reverse_graph = self.reverse_graph()
        new_graph = {}
        print("Creating new graph")
        for key, value in reverse_graph.items():
            new_graph[finishing_time[key]] = [finishing_time[val] for val in value]
        new_graph = Graph(new_graph)

        num_nodes = len(self.list_of_nodes())
        leaders = {}
        explored = []
        print("Computing connected components in new graph")
        for i in list(range(num_nodes, 0, -1)):
            if i not in explored:
                leaders[i] = []
                explored_temp = new_graph.dfs(i, explored=explored, new_explored=[])
                for node in explored_temp:
                    leaders[i].append(node)
                explored = explored + explored_temp
        return leaders
