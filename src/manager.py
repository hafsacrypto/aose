

from dataclasses import dataclass

from aose.src.agent import Agent


@dataclass
class Manager:
	agents = []

	def fetch_online_agents(self):
		online_agents = [agent for agent in self.agents if agent.online]
		return online_agents
	
	def register(self, agent: Agent):
		self.agents.append(agent)