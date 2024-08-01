import networkx as nx
import numpy as np
import random
from modelpy_abm.main import AgentModel
import jsonpickle


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


class ModelFunctions:
    @staticmethod
    def generateInitialData(model: AgentModel):
        initial_data = {"wealth": 1}
        return initial_data

    @staticmethod
    def generateTimestepData(model: AgentModel):
        graph = model.get_graph()

        for _node, node_data in graph.nodes(data=True):
            if node_data["wealth"] > 0:
                other_agent = random.choice(list(graph.nodes.keys()))
                if other_agent is not None:
                    graph.nodes[other_agent]["wealth"] += 1
                    node_data["wealth"] -= 1
        model.set_graph(graph)

    @staticmethod
    def constructModel() -> AgentModel:
        model = AgentModel()
        model.set_initial_data_function(ModelFunctions.generateInitialData)
        model.set_timestep_function(ModelFunctions.generateTimestepData)
        model.update_parameters({"num_nodes": 3})
        return model
