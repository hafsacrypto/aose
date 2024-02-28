


"""
1. Receive request:
	- Get all agents
	- Try to share my data, with other people

2. Make a request:
	- Get the manager to find me all agents with data
	- Request fragment to each agent
		- Trust Agent X or Y will provide that data to me
	
	- Finished

		
3. Another agent. Makes request
	- Already warmed up.


"""











class AgentWorker:
	manager: Manager

	def run(self):
		while True:
			request = self.manager.get()

			if request:
				request_metadata = request.requested_metadata()

				data_to_be_shared = self.repository.get(request_metadata)

				fragments = split(data_to_be_shared)

				other_agents = self.manager.get_online_agents()

				for agent in other_agents:
					agent.request_work(fragments)

	def request_data(self, data):
		agents = self.manager.get_agents(data.meta)

		data_collector = Collector(data.meta)

		for missing_fragment in data_collector.get_missing_fragments():
			fragment = self.agent_pool.request(missing_fragment)

			data_collector.populate(fragment)





class Manager:
	requested_fragments: list

	def request_received(self, fragment):
		for agent in agents:
			agent.fetch(fragment)

		




















class Agent:
	repository: Repository
	manager: Manager

	def worker(self):
		


	def offer(data):
		self.manager.offer(data)

	def split_shards(self, data):
		return [10, 10, 10, 10, 10]

	def receive_request(data):
		agents = self.manager.query_agents()
		shards = self.split_shards()

		for shard, agent in zip(shards, agents):
			agent.offer(shard)




if __name__ == "__main__":
	agent = Agent()
	agent.repository.append(Data())
	agent.worker.run()