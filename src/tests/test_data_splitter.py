

from agent import Agent, DataSplitter
from manager import Manager


def test_data_is_divided_in_chunks():
	data_splitter = DataSplitter()

	data = [1 for _ in range(90)]
 
	chunks = data_splitter.chunks(data)
	assert len(chunks) == 10

def test_agent_manager_returns_online_agents():
	manager = Manager()

	agent1 = Agent("Agent1")
	agent2 = Agent("Agent2")
	agent2.online = False

	manager.register(agent1)
	manager.register(agent2)

	assert manager.fetch_online_agents() == [agent1.name]