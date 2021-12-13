from mesa import Model
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from VoterAgent import VoterAgent
from CandidateAgent import CandidateAgent

"""
Code by the official Mesa tutorial: https://mesa.readthedocs.io/en/master/overview.html
"""

CANDIDATES = ["Kenny", "Alexander", "Ceyhun"]


def calculate_votes(model):
    candidates = {}
    votes = []
    for agent in model.schedule.agents:
        if type(agent) == CandidateAgent:
            candidates[agent.name] = 0
        elif type(agent) == VoterAgent:
            votes.append(agent.vote)
    for vote in votes:
        candidates[vote] += 1
    return max(candidates, key=candidates.get)


class VoterModel(Model):
    """A model with some number of agents."""

    def __init__(self, voters, candidates, width, height):
        self.voters = voters
        self.candidates = candidates
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        for i in range(self.candidates):
            a = CandidateAgent(i, self, CANDIDATES[i])
            self.schedule.add(a)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        for i in range(self.candidates, self.candidates + self.voters):
            a = VoterAgent(i, self, CANDIDATES)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.datacollector = DataCollector(
            model_reporters={"Winner": calculate_votes},
            agent_reporters={"Votes": "vote"})

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
