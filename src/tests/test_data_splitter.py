

from aose.src.agent import DataSplitter


def test_data_is_divided_in_chunks(self):
	data_splitter = DataSplitter()

	assert data_splitter.chunks() == []