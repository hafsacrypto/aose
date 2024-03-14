

from aose.src.agent import DataSplitter


def test_data_is_divided_in_chunks(self):
	data_splitter = DataSplitter()

	data = [1 for _ in range(100)]

	assert data_splitter.chunks(data) == [[1, 1, 1, 1, 1, 1, 1, 1]]