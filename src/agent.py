
from dataclasses import dataclass
import datetime
import time
import numpy as np

class DataSplitter:

	def chunks(self, data):
		array = np.array(data)
		return np.split(array, 10)

class AgentWorker:
	def run(self):
		while True:
			time.sleep(1)
			print(datetime.datetime.now())


if __name__ == "__main__":
	agent = AgentWorker()
	agent.run()