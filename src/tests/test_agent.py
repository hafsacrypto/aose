

from aose.src.agent import Agent


def test_agent_initiative(self):
	agent = Agent("Agent1", True)

	task = Task("SearchForOnlineAgents")
	agent.add_task(task)

	assert agent.initiative() == task