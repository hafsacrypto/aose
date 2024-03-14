from dataclasses import dataclass, field
from agent import Agent

@dataclass
class Manager:
	agents: list = field(default_factory=list)

	def fetch_online_agents(self):
		online_agents = [agent for agent in self.agents if agent.online]
		return online_agents
	
	def register(self, agent: Agent):
		self.agents.append(agent)