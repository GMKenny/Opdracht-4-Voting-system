from mesa import Agent


class CandidateAgent(Agent):
    def __init__(self, unique_id, model, name):
        super().__init__(unique_id, model)
        self.name = name
        self.vote = name

    def step(self):
        pass
