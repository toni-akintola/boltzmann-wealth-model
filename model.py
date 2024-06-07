import networkx as nx
import random


class BoltzmannWealthModel:

    def __init__(self):
        # Define parameters
        self.num_nodes = 3
        self.graph_type = 'complete'

        self.graph: nx.Graph = None

    def initialize_graph(self):
        # Initialize graph shape
        if self.graph_type == 'complete':
            self.graph = nx.complete_graph(self.num_nodes)
        elif self.graph_type == 'cycle':
            self.graph = nx.cycle_graph(self.num_nodes)
        else:
            self.graph = nx.wheel_graph(self.num_nodes)

        # Initialize wealth of all agents
        for node in self.graph.nodes():
            initial_data = {
                'wealth': 1,
            }
            self.graph.nodes[node].update(initial_data)
        return self.graph

    def timestep(self):
        for _node, node_data in self.graph.nodes(data=True):
            if node_data["wealth"] > 0:
                other_agent = random.choice(list(self.graph.nodes.keys()))
                if other_agent is not None:
                    self.graph.nodes[other_agent]["wealth"] += 1
                    node_data["wealth"] -= 1
        return self.graph
