To build the environment:

1) Download Conda (https://docs.anaconda.com/free/miniconda/index.html)

2) Activate your base environment:

	conda activate base

2) Install and run conda-devenv on /aose directory:
	
	conda install conda-devenv --channel conda-forge
	conda devenv
	conda activate agent-oriented-content-provider

Once inside the environment, to run the tests:

	pytest .