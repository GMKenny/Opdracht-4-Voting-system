from matplotlib import pyplot as plt
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from VoterModel import *


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}
    if agent.vote == "Kenny":
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
    elif agent.vote == "Alexander":
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.2
    return portrayal


# grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
# server = ModularServer(VoterModel,
#                       [grid],
#                       "Voter Model",
#                       {"N": 100, "width": 10, "height": 10})
# server.port = 8521  # The default
# server.launch()
voter = VoterModel(10, 3, 10, 10)
for i in range(10):
    voter.step()
votes = voter.datacollector.get_model_vars_dataframe()
print(votes)
