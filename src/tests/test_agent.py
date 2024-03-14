from agent import Agent


def test_agent_initiative():
	agent = Agent("Agent1", True)

	task = Task("SearchForOnlineAgents")
	agent.add_task(task)

	assert agent.initiative() == task