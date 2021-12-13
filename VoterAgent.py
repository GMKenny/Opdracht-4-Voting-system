import random

from mesa import Agent


class VoterAgent(Agent):

    def __init__(self, unique_id, model, candidates):
        super().__init__(unique_id, model)
        self.vote = ""
        self.candidates = candidates
        self.change_vote()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()
        self.change_vote()

    def change_vote(self):
        self.vote = random.choice(self.candidates)
