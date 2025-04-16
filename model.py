import networkx as nx
import numpy as np
import random
from emergent.main import AgentModel


def generateInitialData(model: AgentModel):
    initial_data = {"wealth": 1}
    return initial_data


def generateTimestepData(model: AgentModel):
    graph = model.get_graph()

    for _node, node_data in graph.nodes(data=True):
        if node_data["wealth"] > 0:
            other_agent = random.choice(list(graph.nodes.keys()))
            if other_agent is not None:
                graph.nodes[other_agent]["wealth"] += 1
                node_data["wealth"] -= 1

    model.set_graph(graph)


def constructModel() -> AgentModel:
    model = AgentModel()
    model.set_initial_data_function(generateInitialData)
    model.set_timestep_function(generateTimestepData)
    model.update_parameters({"num_nodes": 3})
    model["variations"] = ["base"]
    return model