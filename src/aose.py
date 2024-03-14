"""
Basic unit									object									agent
Parameters defining state of basic unit		unconstrained							beliefs, commitments, capabilities, choices, ...
Process of computation						message passing and response methods	message passing and response methods
Types of message							unconstrained							inform, request, offer, promise, decline, ...
Constraints on methods						none									honesty, consistency, ...


Agent:

	- Autonomy
		- Provide work.
	- Reactivity
	- Pro-activity
	- Social ability
	
	Agent 1:
		- Movie1.mp4 -> 5GB
			- Split into N shards of 50mb each.
			- 

	Agent 2:
		- Up to 10GB

	Agent 3:

	Agent 4:

	Agent 5:

	Agent 6:

	Agent 7:

	Agent 8:


	Agent 2:
		- Requests Movie1.mp4
		- Creates a commitment from all the online agents
			For what?
				- They are gonna help make this content available


	With time:
		- Increase availability of data
		- Bigger fragmentation 

	Commitments:
		- Shared responsability
		- Sharing data
		- Storing
			- TTL
	
	Properties:
		- If Movie1.mp4 gets frequently requested, then the agents are more likely to have the content to share
		- As soon as the data isn't requested anymore, its availability will drop, until more requests arrive






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



def main():
	agent = Agent()
	agent.add_task(Content("Naruto"))
	agent.run()


if __name__ == "__main__":
	main()
