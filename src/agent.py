
import datetime
import time

class DataSplitter:

	def chunks(self):
		return []


class AgentWorker:
	def run(self):
		while True:
			time.sleep(1)
			print(datetime.datetime.now())


if __name__ == "__main__":
	agent = AgentWorker()
	agent.run()