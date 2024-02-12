"""
Basic unit									object									agent
Parameters defining state of basic unit		unconstrained							beliefs, commitments, capabilities, choices, ...
Process of computation						message passing and response methods	message passing and response methods
Types of message							unconstrained							inform, request, offer, promise, decline, ...
Constraints on methods						none									honesty, consistency, ...


Agent:

	Beliefs:
		- My download speed: which can be influenced periodically
		- My upload speed: which can also be influenced
		- List of peers

		Trusts:
			- If an Agent promised me too much but didn't deliver. Could we model a trust ranking or etc?
				- Influences:
					- Creating more tasks that this agent is going to execute:
						- self.queue.put(ContentFetcher(movie))
						- Choose to drop some connections. Keep them alive, because he's still providing content, etc.

	Goals:
		- To send data to other Agents
		- To receive the data I need from other Agents:
			- I need to request. Who to?

	Rules:
		- TBD

	Constraints:
		- TBD

	Choices:
		- Which choices can an agent have

	Actions:
		- Inform about my Video I wanna share
		- Request some content that my user wants
"""
import queue
import time


class Repository:
	pass


class AgentManager:

	def __init__(self):
		self.repository = Repository()


class Content:

	def __init__(self, content_name):
		self.content_name = content_name



class ContentFetcher:

	def __init__(self):
		pass

	def run(self):
		# 1. Ask the ContentManager for stuff
		response = self.request()
		response.peers
		response.size

		content.size = 2000000000
		content.length = 60


class ContentPublisher:

	def __init__(self):
		pass


class Agent:

	def __init__(self):
		self.beliefs = []
		self.queue = queue.Queue()
		self.agent_manager = AgentManager()

	def run(self):

		print("Agent running")
		while True:
			print("Agent fetching task")
			task = self.queue.get()

			if task.finished():
				# Decide what else to do
			else:
				task.run()

				content_fetcher = ContentFetcher()


			print("Task fetched", task)


	def add_task(self, task):
		self.queue.put(task)


def main():
	agent = Agent()
	agent.add_task(Content("Naruto"))
	agent.run()


if __name__ == "__main__":
	main()
