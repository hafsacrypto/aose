
from dataclasses import dataclass, field
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


@dataclass
class Agent:
	name: str
	online: bool = True
	tasks: list = field(default_factory=list)

	def initiative(self):
		"""Should decide what to do based on the current set of tasks it possess"""

if __name__ == "__main__":
	agent = AgentWorker()
	agent.run()